"""
08- Log Security & Secret Detection at Scale

You are building a log-processing system for a large-scale production environment where millions of log 
lines are generated per minute across thousands of services.
Some logs may accidentally leak sensitive credentials, such as:
Cloud access keys (for example, AWS access keys)
Application secret keys
JWT authentication tokens

Problem Statement
Design and implement a function that scans a stream or batch of log lines and identifies lines that 
contain potentially sensitive secrets.
Secrets should be detected using pattern matching (for example, via regular expressions).
The function should return only the flagged log lines that contain secrets.
"""
import re

def scan_logs_for_secrets(logs):
    """
    Scan log lines to find lines with sensitive information (secrets).

    Args:
        logs (list of str): A list of log lines to check.

    Returns:
        list: Lines that contain secrets like AWS keys, secret keys, or JWTs.
    """
    # List of patterns to find secrets
    secret_patterns = [
        r'AKIA[0-9A-Z]{16}',  # AWS Access Key (e.g., AKIA1234567890ABCDEF)
        r'(?i)secret[_-]?key\s*=\s*[A-Za-z0-9/+=]{16,}',  # Generic secret key (e.g., secret_key=abc123...)
        r'eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+'  # JWT (e.g., eyJhbGciOiJI...)
    ]

    # Create a list to hold compiled patterns
    compiled_patterns = []
    for pattern in secret_patterns:
        compiled_patterns.append(re.compile(pattern))

    # Create a list to hold lines with secrets
    flagged_lines = []
    for line in logs:
        # Check if any pattern matches the line
        for pattern in compiled_patterns:
            if pattern.search(line):
                flagged_lines.append(line)
                break  # Stop checking patterns once a match is found

    return flagged_lines

logs = [
    "INFO user logged in",
    "DEBUG AWS key = AKIA1234567890ABCD",
    "WARN secret_key=abcd1234abcd1234",
    "INFO token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abc.def"
]

print(scan_logs_for_secrets(logs))
# Expected:
# [
#   "DEBUG AWS key = AKIA1234567890ABCD",
#   "WARN secret_key=abcd1234abcd1234",
#   "INFO token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abc.def"
# ]

# “I scan logs using pre-compiled regex patterns to efficiently detect leaked credentials, ensuring 
# low latency, easy extensibility, and safe handling of sensitive data at scale.”