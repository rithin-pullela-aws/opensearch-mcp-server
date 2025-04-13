#!/usr/bin/env python3
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.opensearch.client import client

def test_connection():
    """Test the connection to OpenSearch cluster."""
    try:
        # Test health check
        health = client.health_check()
        print(f"Cluster health: {health['status']}")
        
        # Test listing indices
        indices = client.list_indices()
        print("\nAvailable indices:")
        for index in indices:
            print(f"- {index}")
            
        return True
    except Exception as e:
        print(f"Error connecting to OpenSearch: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1) 