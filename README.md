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

## Configuration

All connectors use **environment variables** for configuration. Each connector documents its expected variables in the `connect()` docstring.

Example:

```bash
export PG_HOST=localhost
export PG_USER=myuser
export PG_PASSWORD=secret
export PG_DATABASE=mydb
python postgresql_connector.py
```

If environment variables are not set, connectors fall back to placeholder defaults (`<username>`, `<password>`, etc.).

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
- DuckDB
- CockroachDB
- Firebird

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
- Google Bigtable
- Azure Table Storage

### NoSQL Databases
- MongoDB
- Redis
- Cassandra
- ScyllaDB
- Couchbase
- RethinkDB
- ArangoDB
- EdgeDB
- SurrealDB
- YugabyteDB
- rqlite

### Graph Databases
- Neo4j
- Neptune (Gremlin)
- JanusGraph
- Dgraph
- OrientDB
- TigerGraph
- Nebula Graph
- Gremlin (Generic)

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
- Dragonfly
- Valkey

### Specialized
- HBase
- Apache Ignite
- Tarantool
- VoltDB
- MonetDB
- Hazelcast
- Rockset
- Stardog (RDF)
- Salesforce
- Odoo

### File Format Readers
- Parquet
- Feather
- HDF5
- RDF (Triplestore)

## Features

- **98 database connectors** covering relational, NoSQL, cloud, graph, vector, and specialized databases
- **Environment variable configuration** — no hardcoded credentials; all config via `os.environ.get()`
- **Error handling** — all connectors catch and report connection failures gracefully
- **Type hints and docstrings** — every `connect()` function has return type annotations and documentation
- **Minimal dependencies** — each connector uses only the required client library
- **Consistent interface** — all connectors expose a `connect()` function
- **Ready-to-run examples** — each script includes a `__main__` block with sample usage

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
    has_docstring = isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant)
    status = '✓' if 'connect' in functions and has_docstring else '✗'
    print(f'{status} {file.name}')
"
```
