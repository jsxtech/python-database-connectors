# Python Database Connectors

Individual connector scripts for 98 databases, data stores, and streaming platforms.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Each script can be run independently:

```bash
python mysql_connector.py
python postgresql_connector.py
# etc.
```

## Databases Supported

### Relational Databases
- MySQL
- MariaDB
- PostgreSQL
- MS SQL Server
- Oracle
- SQLite
- IBM DB2
- Teradata
- Vertica
- SingleStore

### Cloud Databases
- Aurora PostgreSQL
- Google AlloyDB
- Google BigQuery
- Google Cloud Spanner
- Google Firestore
- Azure Cosmos DB
- Supabase
- Databricks
- Snowflake
- Firebolt
- DynamoDB
- Cloudflare D1
- Neon
- PlanetScale
- Turso
- Fauna
- TiDB

### NoSQL Databases
- MongoDB
- Redis
- Cassandra
- ScyllaDB
- Couchbase
- RethinkDB
- ArangoDB
- Firebird
- DuckDB
- EdgeDB
- SurrealDB
- YugabyteDB
- Dragonfly
- Valkey
- rqlite

### Graph Databases
- Neo4j
- Neptune
- JanusGraph
- Dgraph
- OrientDB
- TigerGraph
- Nebula Graph

### Vector Databases
- Qdrant
- Weaviate
- Pinecone
- ChromaDB
- Milvus
- LanceDB
- Marqo

### Search Engines
- Elasticsearch
- OpenSearch
- Apache Solr
- Meilisearch
- Typesense

### Time Series
- InfluxDB
- TimescaleDB
- QuestDB
- AWS Timestream

### Big Data / Analytics
- Apache Hive
- Apache Spark SQL
- Presto
- Trino
- Impala
- ClickHouse
- CockroachDB
- Apache Druid
- Exasol
- Kinetica

### Message Queues / Streaming
- Kafka
- RabbitMQ
- Apache Pulsar
- NATS

### Key-Value Stores
- etcd
- Memcached

### Specialized Databases
- HBase
- Apache Ignite
- Tarantool
- VoltDB
- MonetDB
- Hazelcast
- Rockset
- Stardog (RDF)
- RDF (Triplestore)
- Azure Table Storage
- Google Bigtable
- Gremlin (Graph Query)
- Parquet (File Format)
- Feather (File Format)
- HDF5 (File Format)
- Salesforce
- Odoo

## Configuration

Replace placeholders in each script:
- `<username>`, `<password>`, `<database>`, `<host>`, etc.

## Features

- **98 database connectors** covering relational, NoSQL, cloud, graph, vector, and specialized databases
- **Minimal dependencies** - each connector uses only the required client library
- **Consistent interface** - all connectors expose a `connect()` function
- **Ready-to-run examples** - each script includes a `__main__` block with sample usage
- **Easy to extend** - simple structure makes it easy to add new connectors

## Testing

Validate all connectors have proper structure:

```bash
python3 -c "
import ast
from pathlib import Path

for file in sorted(Path('.').glob('*_connector.py')):
    with open(file) as f:
        tree = ast.parse(f.read())
    functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    status = '✓' if 'connect' in functions else '✗'
    print(f'{status} {file.name}')
"
```
