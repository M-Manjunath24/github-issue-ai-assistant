from urllib.parse import urlparse


def parse_github_repo(repo_url: str):
    """
    Extract owner and repo name from GitHub URL.
    Example:
    https://github.com/facebook/react -> (facebook, react)
    """
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")

    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner = path_parts[0]
    repo = path_parts[1]

    return owner, repo
