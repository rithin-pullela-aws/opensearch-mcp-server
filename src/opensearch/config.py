from typing import Optional
import os
from dataclasses import dataclass

@dataclass
class OpenSearchConfig:
    """Configuration for OpenSearch connection."""
    host: str
    port: int
    username: Optional[str] = None
    password: Optional[str] = None
    use_ssl: bool = False
    verify_certs: bool = False
    ca_certs: Optional[str] = None

    @classmethod
    def from_env(cls) -> 'OpenSearchConfig':
        """Create configuration from environment variables."""
        return cls(
            host=os.getenv('OPENSEARCH_HOST', 'localhost'),
            port=int(os.getenv('OPENSEARCH_PORT', '9200')),
            username=os.getenv('OPENSEARCH_USERNAME', 'admin'),
            password=os.getenv('OPENSEARCH_PASSWORD', 'admin'),
            use_ssl=os.getenv('OPENSEARCH_USE_SSL', 'false').lower() == 'true',
            verify_certs=os.getenv('OPENSEARCH_VERIFY_CERTS', 'false').lower() == 'true',
            ca_certs=os.getenv('OPENSEARCH_CA_CERTS')
        )

# Default configuration instance
config = OpenSearchConfig.from_env() 