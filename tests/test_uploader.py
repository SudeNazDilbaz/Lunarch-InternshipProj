from secure_uploader.uploader import secure_upload

test_cases = [
    (
        "tests/sample_files/sample.jpg",
        "my photo!.jpg",
        "uploads"
    ),
    (
        "tests/sample_files/sample.png",
        "../../../profile.png",
        "uploads"
    ),
    (
        "tests/sample_files/sample_exe_header.bin",
        "virus.exe",
        "uploads"
    ),
]

print("=== Uploader Test Results ===\n")

for source_file, original_name, upload_dir in test_cases:
    result = secure_upload(source_file, original_name, upload_dir)
    print(f"{original_name} -> {result}")

print("\n=== Test Completed ===")