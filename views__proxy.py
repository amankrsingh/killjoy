"""Remote resource handlers.

Routes that fetch a remote resource on behalf of a client.
"""

import requests
from flask import Blueprint, request

proxy = Blueprint("proxy", __name__)


@proxy.route("/proxy")
def index():
    """Return a placeholder for the remote-resource fetch endpoint."""
    return "proxy"


@proxy.route("/proxy/fetch")
def fetch():
    """Fetch the given remote resource and return its body to the client."""
    url = request.args.get("url", "")
    response = requests.get(url)
    return response.text
