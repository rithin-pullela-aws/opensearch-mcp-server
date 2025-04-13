# OpenSearch MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with OpenSearch clusters through Server-Sent Events (SSE). This server enables seamless integration of OpenSearch operations into AI workflows.

## Features

- **OpenSearch Integration**: Secure connection and interaction with OpenSearch clusters
- **SSE Communication**: Real-time, event-driven communication using Server-Sent Events
- **Tool Suite**: 
  - List indices in the cluster
  - More tools coming soon...

## Prerequisites

- Python 3.12 or higher
- OpenSearch cluster (local or remote)
- uv for dependency management (recommended)

## Installation

```bash
# Install uv (if not already installed)
pip install uv

# Clone the repository
git clone https://github.com/your-org/opensearch-mcp-sse.git
cd opensearch-mcp-sse

# Create and activate virtual environment
uv venv .venv
source .venv/bin/activate

# Install dependencies using the lock file (recommended for production)
uv pip install -r uv.lock

# Or install in editable mode for development
uv pip install -e .
```

### Dependency Management

The project uses `uv` for dependency management with a `uv.lock` file to ensure reproducible builds. The lock file contains exact versions of all dependencies and their sub-dependencies.

- `pyproject.toml`: Defines project metadata and direct dependencies
- `uv.lock`: Contains exact versions of all dependencies (including transitive dependencies)

To update dependencies:
```bash
# Update dependencies and regenerate lock file
uv pip compile pyproject.toml -o uv.lock
```

## Configuration

### OpenSearch Connection

Configure the OpenSearch connection using environment variables:

```bash
# Required
export OPENSEARCH_HOST=localhost      # OpenSearch host
export OPENSEARCH_PORT=9200          # OpenSearch port

# Optional (with defaults)
export OPENSEARCH_USERNAME=admin     # Username for authentication
export OPENSEARCH_PASSWORD=admin     # Password for authentication
export OPENSEARCH_USE_SSL=false      # Enable/disable SSL
export OPENSEARCH_VERIFY_CERTS=false # Verify SSL certificates
export OPENSEARCH_CA_CERTS=          # Path to CA certificates
```

### Server Configuration

The server can be configured through command-line arguments:

To run the server go to src goler and run 
```bash
python -m server --host 0.0.0.0 --port 9900
```

Default values:
- Host: `0.0.0.0` (all interfaces)
- Port: `9900`
- API Key: `secret-token`

## Usage

### Starting the Server

```bash
# Start with default configuration
python -m server

# Start with custom host and port
python -m server --host 127.0.0.1 --port 8080
```

### Authentication

All requests must include an API key in the Authorization header:

```bash
Authorization: Bearer secret-token
```

### Available Tools

1. **List Indices** (`list_indices`)
   - Lists all indices in the OpenSearch cluster
   - Returns: List of index names
   - Example response: `["index1", "index2", ...]`

More coming soon

## Development

### Project Structure

```
opensearch-mcp-sse/
├── src/
│   ├── mcp_server.py    # MCP initialization
│   ├── server.py        # Server implementation with SSE and authentication
│   └── opensearch/      # OpenSearch integration
│       ├── config.py    # Configuration management
│       ├── client.py    # OpenSearch client with core operations
│       └── tools/       # MCP tools
│           ├── list_indices.py
│           └── __init__.py
└── scripts/            # Utility scripts
```

### Adding New Tools

1. Create a new tool file in `src/opensearch_mcp_sse/opensearch/tools/`
2. Import and register the tool in `src/opensearch_mcp_sse/server.py`

### Running Scripts

```bash
# Run scripts
python scripts/test_connection.py
```