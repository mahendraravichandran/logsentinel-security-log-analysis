import re
from collections import defaultdict

LOG_PATTERN = re.compile(
    r'^(?P<date>\d{4}-\d{2}-\d{2}) '
    r'(?P<time>\d{2}:\d{2}:\d{2}) '
    r'(?P<level>\w+) '
    r'(?P<action>Successful login|Failed login) '
    r'for user (?P<user>\w+) '
    r'from (?P<ip>[0-9\.]+)$'
)

FAILED_THRESHOLD = 5


def parse_log_line(line: str):
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None
    return match.groupdict()


def analyze_log_file(path: str):
    failed_logins = defaultdict(int)
    total = 0
    parsed = 0

    with open(path, "r") as f:
        for line in f:
            total += 1
            data = parse_log_line(line)
            if not data:
                continue
            parsed += 1

            if data["action"] == "Failed login":
                failed_logins[data["ip"]] += 1

    return {
        "total": total,
        "parsed": parsed,
        "failed_logins": failed_logins,
    }


def main():
    log_path = "sample_auth.log"
    result = analyze_log_file(log_path)
    print_report(result)

if __name__ == "__main__":
    main()
