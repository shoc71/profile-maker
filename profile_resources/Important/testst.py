import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def get_disallowed_paths(base_url):
    """
    Fetches and returns the disallowed paths from the robots.txt of a given base_url.
    
    Args:
    - base_url (str): The base URL of the website whose robots.txt file to check.
    
    Returns:
    - disallowed_paths (list): List of disallowed paths.
    """
    robots_url = urljoin(base_url, '/robots.txt')

    try:
        response = requests.get(robots_url)
        response.raise_for_status()
        robots_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {robots_url}: {e}")
        return []

    # Parse robots.txt content to find disallowed paths
    disallowed_paths = []
    lines = robots_content.splitlines()

    for line in lines:
        if line.strip().lower().startswith('disallow:'):
            path = line.strip().split(':', 1)[1].strip()
            disallowed_paths.append(path)

    return disallowed_paths

# Example usage
base_url = 'https://www.merriam-webster.com/'
disallowed_paths = get_disallowed_paths(base_url)

print("Disallowed Paths:")
for path in disallowed_paths:
    print(path)
