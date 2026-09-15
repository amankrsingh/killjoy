"""Process helpers.

Utilities for running a report job as an external process.
"""

import subprocess


def run_report_job(name):
    """Run the report generator for the given job.

    Launches the report generator tool for the named job and returns its
    completed process handle so the caller can inspect the result.
    """
    return subprocess.run(f"generate_report {name}", shell=True)
