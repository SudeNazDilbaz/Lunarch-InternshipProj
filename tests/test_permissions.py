from secure_uploader.permissions import set_safe_permissions


def main():
    test_files = [
        "tests/sample_files/sample.jpg",
        "tests/sample_files/missing_file.jpg",
    ]

    print("=" * 50)
    print("Permissions Test Results")
    print("=" * 50)

    for test_file in test_files:
        result = set_safe_permissions(test_file)
        print(f"{test_file} -> {result}")

    print("\nAll permissions tests completed.")


if __name__ == "__main__":
    main()