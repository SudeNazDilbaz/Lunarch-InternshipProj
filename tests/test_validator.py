from secure_uploader.validator import is_allowed_file

files = [
    "tests/sample_files/sample.jpg",
    "tests/sample_files/sample.png",
    "tests/sample_files/sample.pdf",
    "tests/sample_files/sample_exe_header.bin",
    "tests/sample_files/unknown.txt",
]

print("=== Validator Test Results ===\n")

for file in files:
    result = is_allowed_file(file)
    print(f"{file} -> {result}")

print("\n=== Test Completed ===")