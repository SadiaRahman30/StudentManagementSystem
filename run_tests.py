import os
import sys
import subprocess

test_files = [
    "tests/test_1_page_load.py",
    "tests/test_2_invalid_login.py",
    "tests/test_3_valid_login.py",
    "tests/test_4_registration.py",
    "tests/test_5_dashboard.py",
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    failed = False

    for test in test_files:
        path = os.path.join(base_dir, test)
        print(f"Running {test}...")
        res = subprocess.run([sys.executable, path], cwd=base_dir)
        if res.returncode != 0:
            print(f"FAILED: {test}")
            failed = True
        else:
            print(f"PASSED: {test}")

    if failed:
        print("\nSome tests failed.")
        sys.exit(1)
    else:
        print("\nAll tests passed successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
