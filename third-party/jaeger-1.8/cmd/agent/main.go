// Copyright (c) 2017 Uber Technologies, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"go.uber.org/zap"

	"github.com/jaegertracing/jaeger/cmd/agent/app"
	"github.com/jaegertracing/jaeger/cmd/agent/app/reporter/tchannel"
	"github.com/jaegertracing/jaeger/cmd/flags"
	"github.com/jaegertracing/jaeger/pkg/config"
	"github.com/jaegertracing/jaeger/pkg/metrics"
	"github.com/jaegertracing/jaeger/pkg/version"
)

func main() {
	v := viper.New()
	var command = &cobra.Command{
		Use:   "jaeger-agent",
		Short: "Jaeger agent is a local daemon program which collects tracing data.",
		Long:  `Jaeger agent is a daemon program that runs on every host and receives tracing data submitted by Jaeger client libraries.`,
		RunE: func(cmd *cobra.Command, args []string) error {
			err := flags.TryLoadConfigFile(v)
			if err != nil {
				return err
			}

			sFlags := new(flags.SharedFlags).InitFromViper(v)
			logger, err := sFlags.NewLogger(zap.NewProductionConfig())
			if err != nil {
				return err
			}

			tchanRep := tchannel.NewBuilder().InitFromViper(v, logger)
			builder := new(app.Builder).InitFromViper(v)
			mBldr := new(metrics.Builder).InitFromViper(v)

			mFactory, err := mBldr.CreateMetricsFactory("jaeger")
			if err != nil {
				logger.Fatal("Could not create metrics", zap.Error(err))
			}
			mFactory = mFactory.Namespace("agent", nil)

			cp, err := tchannel.NewCollectorProxy(tchanRep, mFactory, logger)
			if err != nil {
				logger.Fatal("Could not create collector proxy", zap.Error(err))
			}

			// TODO illustrate discovery service wiring

			agent, err := builder.CreateAgent(cp, logger, mFactory)
			if err != nil {
				return errors.Wrap(err, "Unable to initialize Jaeger Agent")
			}

			if h := mBldr.Handler(); mFactory != nil && h != nil {
				logger.Info("Registering metrics handler with HTTP server", zap.String("route", mBldr.HTTPRoute))
				agent.GetServer().Handler.(*http.ServeMux).Handle(mBldr.HTTPRoute, h)
			}

			logger.Info("Starting agent")
			if err := agent.Run(); err != nil {
				return errors.Wrap(err, "Failed to run the agent")
			}
			select {}
		},
	}

	command.AddCommand(version.Command())

	config.AddFlags(
		v,
		command,
		flags.AddConfigFileFlag,
		flags.AddLoggingFlag,
		app.AddFlags,
		tchannel.AddFlags,
		metrics.AddFlags,
	)

	if err := command.Execute(); err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}
}
