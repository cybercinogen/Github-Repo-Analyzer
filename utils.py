from urllib.parse import urlparse
from typing import Tuple, Optional

# --- URL PARSING ---
def parse_github_url(url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parses a GitHub repo URL and returns (owner, repo).
    Returns (None, None) if the URL is invalid.
    """
    try:
        # Parse the URL into its components
        parsed = urlparse(url)
        
        # Check if the URL is a valid GitHub URL
        if parsed.netloc not in ('github.com', 'www.github.com'):
            return None, None
        
        # Split the URL path into its parts
        path_parts = parsed.path.strip('/').split('/')
        
        # Check if the URL path has at least two parts (owner and repo)
        if len(path_parts) < 2:
            return None, None
        
        # Extract the owner and repo from the URL path
        owner, repo = path_parts[0], path_parts[1]
        
        # Return the owner and repo
        return owner, repo
    except Exception:
        # Return None if an exception occurs during parsing
        return None, None
