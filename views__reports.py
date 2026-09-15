"""Report request handlers.

Routes that build and return report pages for the reporting service.
"""

from flask import Blueprint, request

reports = Blueprint("reports", __name__)


@reports.route("/reports")
def index():
    """Return a landing page for the reports section."""
    return "reports"


@reports.route("/reports/greeting")
def greeting():
    """Greet the named user on the reports landing page."""
    username = request.args.get("name", "")
    return f"<h1>Hello {username}</h1>"
