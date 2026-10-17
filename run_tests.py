#!/usr/bin/env python3
"""
Automated Test Suite Runner for Student Management System CI/CD Pipeline.
Runs all Selenium headless tests and returns exit code 0 on success, 1 on failure.
"""

import os
import sys
import subprocess
import time

TEST_FILES = [
    "tests/test_1_page_load.py",
    "tests/test_2_invalid_login.py",
    "tests/test_3_valid_login.py",
    "tests/test_4_registration.py",
    "tests/test_5_dashboard.py",
]

def run_all_tests():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 65)
    print("  Student Management System - Automated CI Test Suite")
    print("=" * 65)

    results = []
    overall_start = time.time()

    for test_path in TEST_FILES:
        full_path = os.path.join(project_dir, test_path)
        test_name = os.path.basename(test_path)
        print(f"\n▶ Running {test_name} ...")
        
        start = time.time()
        process = subprocess.run(
            [sys.executable, full_path],
            cwd=project_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        elapsed = time.time() - start

        if process.returncode == 0:
            print(f"✔ {test_name} PASSED ({elapsed:.2f}s)")
            results.append((test_name, True, elapsed, process.stdout))
        else:
            print(f"✖ {test_name} FAILED ({elapsed:.2f}s)")
            print("-" * 50)
            print(process.stdout.strip())
            print("-" * 50)
            results.append((test_name, False, elapsed, process.stdout))

    overall_elapsed = time.time() - overall_start

    print("\n" + "=" * 65)
    print("                   TEST EXECUTION SUMMARY")
    print("=" * 65)
    passed_count = sum(1 for _, passed, _, _ in results if passed)
    total_count = len(results)

    for name, passed, elapsed, _ in results:
        status_symbol = "✔ PASSED" if passed else "✖ FAILED"
        print(f" {name:<26} : {status_symbol} ({elapsed:.2f}s)")

    print("-" * 65)
    print(f" Total: {passed_count}/{total_count} Passed in {overall_elapsed:.2f}s")
    print("=" * 65)

    if passed_count == total_count:
        print("\n🎉 ALL TESTS PASSED! CI BUILD VERIFIED.")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED! CI BUILD BLOCKED.")
        sys.exit(1)

if __name__ == "__main__":
    run_all_tests()
