from typing import List, Optional, Dict, Any
from opensearchpy import OpenSearch, RequestsHttpConnection
from opensearchpy.exceptions import OpenSearchException

from .config import config

class OpenSearchClient:
    """Client for OpenSearch operations."""
    
    def __init__(self):
        """Initialize OpenSearch client with configuration."""
        self._client = None
        
    @property
    def client(self) -> OpenSearch:
        """Get OpenSearch client, creating it if necessary."""
        if self._client is None:
            self._client = self._create_client()
        return self._client
    
    def _create_client(self) -> OpenSearch:
        """Create and return an OpenSearch client."""
        auth = None
        if config.username and config.password:
            auth = (config.username, config.password)
            
        return OpenSearch(
            hosts=[{'host': config.host, 'port': config.port}],
            http_auth=auth,
            use_ssl=config.use_ssl,
            verify_certs=config.verify_certs,
            ca_certs=config.ca_certs,
            connection_class=RequestsHttpConnection
        )
    
    def list_indices(self) -> List[str]:
        """
        List all indices in the OpenSearch cluster.
        
        Returns:
            List[str]: List of index names
            
        Raises:
            OpenSearchException: If there's an error communicating with OpenSearch
        """
        try:
            response = self.client.cat.indices(format='json')
            return [index['index'] for index in response]
        except OpenSearchException as e:
            raise OpenSearchException(f"Failed to list indices: {str(e)}")
    
    def get_index_info(self, index_name: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific index.
        
        Args:
            index_name: Name of the index to get information about
            
        Returns:
            Dict[str, Any]: Index information
            
        Raises:
            OpenSearchException: If there's an error communicating with OpenSearch
        """
        try:
            return self.client.indices.get(index=index_name)
        except OpenSearchException as e:
            raise OpenSearchException(f"Failed to get index info for {index_name}: {str(e)}")
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check the health of the OpenSearch cluster.
        
        Returns:
            Dict[str, Any]: Cluster health information
            
        Raises:
            OpenSearchException: If there's an error communicating with OpenSearch
        """
        try:
            return self.client.cluster.health()
        except OpenSearchException as e:
            raise OpenSearchException(f"Failed to get cluster health: {str(e)}")

# Global instance of the client
client = OpenSearchClient() 