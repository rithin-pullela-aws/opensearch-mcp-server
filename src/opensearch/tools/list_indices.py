from typing import  List
from mcp_server import mcp

from ..client import client

def list_indices() -> List[str]:
    """
    List all indices in the OpenSearch cluster.
    
    Returns:
        List[str]: List of index names
        
    Raises:
        OpenSearchException: If there's an error communicating with OpenSearch
    """
    return client.list_indices() 