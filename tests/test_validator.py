from secure_uploader.validator import is_allowed_file


def main():
    files = [
        "tests/sample_files/sample.jpg",
        "tests/sample_files/sample.png",
        "tests/sample_files/sample.pdf",
        "tests/sample_files/sample_exe_header.bin",
        "tests/sample_files/unknown.txt",
        "tests/sample_files/empty.bin",
        "tests/sample_files/fake_jpg.bin",
        "tests/sample_files/fake_image.jpg",
    ]

    print("=" * 50)
    print("Validator Test Results")
    print("=" * 50)

    for file_path in files:
        result = is_allowed_file(file_path)
        print(f"{file_path} -> {result}")

    print("\nAll validator tests completed.")


if __name__ == "__main__":
    main()