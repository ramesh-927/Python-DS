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