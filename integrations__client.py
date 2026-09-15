"""Third-party client configuration.

Holds connection settings for the external service the reporting app talks to.
"""

API_KEY = "sk-demo-1234567890abcdef"

SERVICE_URL = "https://api.example.com/v1"


def get_client():
    """Return a configured client for the external service.

    Builds the third-party client config from the module settings.
    """
    return {
        "base_url": SERVICE_URL,
        "api_key": API_KEY,
        "timeout": 30,
    }
