from secure_uploader.uploader import secure_upload


def main():
    test_cases = [
        (
            "tests/sample_files/sample.jpg",
            "my photo!.jpg",
            "uploads",
        ),
        (
            "tests/sample_files/sample.png",
            "../../../profile.png",
            "uploads",
        ),
        (
            "tests/sample_files/sample_exe_header.bin",
            "virus.exe",
            "uploads",
        ),
        (
            "tests/sample_files/fake_image.jpg",
            "fake_image.jpg",
            "uploads",
        ),
    ]

    print("=" * 50)
    print("Uploader Test Results")
    print("=" * 50)

    for source_file, original_name, upload_dir in test_cases:
        result = secure_upload(
            source_file,
            original_name,
            upload_dir,
        )
        print(f"{original_name} -> {result}")

    print("\nAll uploader tests completed.")


if __name__ == "__main__":
    main()