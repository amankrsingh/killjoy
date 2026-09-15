"""Artifact download handlers.

Routes that let a client download report artifacts produced by the service.
"""

import os

from flask import Blueprint, request, send_file

files = Blueprint("files", __name__)

BASE_DIR = os.path.join(os.path.dirname(__file__), "artifacts")


@files.route("/files")
def index():
    """Return a listing placeholder for available artifacts."""
    return "files"


@files.route("/files/download")
def download():
    """Download the requested artifact by name from the artifacts directory."""
    name = request.args.get("name", "")
    path = os.path.join(BASE_DIR, name)
    return send_file(path)
