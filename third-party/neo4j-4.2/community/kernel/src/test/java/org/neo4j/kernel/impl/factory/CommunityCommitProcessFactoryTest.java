/*
 * Copyright (c) 2002-2020 "Neo4j,"
 * Neo4j Sweden AB [http://neo4j.com]
 *
 * This file is part of Neo4j.
 *
 * Neo4j is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.neo4j.kernel.impl.factory;

import org.junit.jupiter.api.Test;

import org.neo4j.configuration.Config;
import org.neo4j.configuration.GraphDatabaseSettings;
import org.neo4j.kernel.impl.api.ReadOnlyTransactionCommitProcess;
import org.neo4j.kernel.impl.api.TransactionCommitProcess;
import org.neo4j.kernel.impl.api.TransactionRepresentationCommitProcess;
import org.neo4j.kernel.impl.transaction.log.TransactionAppender;
import org.neo4j.storageengine.api.StorageEngine;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;

class CommunityCommitProcessFactoryTest
{
    @Test
    void createReadOnlyCommitProcess()
    {
        CommunityCommitProcessFactory factory = new CommunityCommitProcessFactory();

        Config config = Config.defaults( GraphDatabaseSettings.read_only, true );

        TransactionCommitProcess commitProcess = factory.create( mock( TransactionAppender.class ),
                mock( StorageEngine.class ), config );

        assertThat( commitProcess ).isInstanceOf( ReadOnlyTransactionCommitProcess.class );
    }

    @Test
    void createRegularCommitProcess()
    {
        CommunityCommitProcessFactory factory = new CommunityCommitProcessFactory();

        TransactionCommitProcess commitProcess = factory.create( mock( TransactionAppender.class ),
                mock( StorageEngine.class ), Config.defaults() );

        assertThat( commitProcess ).isInstanceOf( TransactionRepresentationCommitProcess.class );
    }
}
