import os
from datetime import datetime

# Iterate through test cases, log each result with timestamp,
# count passed/failed tests, and write a summary to a log file.


DOWNLOAD_DIR = "logs"
test_cases = [
    {"name": "test_login_valid_user", "status": "PASS"},
    {"name": "test_login_wrong_password", "status": "FAIL"},
    {"name": "test_upload_file", "status": "PASS"},
    {"name": "test_download_report", "status": "FAIL"},
]

os.makedirs (DOWNLOAD_DIR, exist_ok=True)
file_path = os.path.join(DOWNLOAD_DIR, "test_run.log")

passed = 0
fail = 0
total = len(test_cases)
with open (file_path, "a") as f:
    for test in test_cases:

        name = test["name"]
        status = test["status"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = (f" {current_time} {status} - {name} \n")
        f.write(line)

        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            fail += 1

    summary = (f"\n--- SUMMARY --- \n Total: {total} | Passed: {passed}, Failed: {fail}")

    f.write(summary)

print(line+summary)

