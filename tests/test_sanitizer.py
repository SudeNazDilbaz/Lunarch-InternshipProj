from secure_uploader.sanitizer import clean_filename, get_safe_path

filenames = [
    "../../../secret.txt",
    "..\\..\\windows.ini",
    "my photo!.jpg",
    "report#$%.pdf",
    "...",
    "normal_file.png",
]

print("=" * 50)
print("Sanitizer Test Results")
print("=" * 50)

for filename in filenames:
    print(f"{filename} -> {clean_filename(filename)}")

print("\nSafe Path Test")
print(get_safe_path("uploads", "../../../secret.txt"))

print("\nAll tests completed.")