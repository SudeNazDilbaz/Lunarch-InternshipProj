from secure_uploader.permissions import set_safe_permissions
import os

test_file = "tests/sample_files/sample.jpg"

print("=" * 50)
print("Permissions Test Results")
print("=" * 50)

result = set_safe_permissions(test_file)

if result:
    print(f"Safe permissions applied to: {test_file}")
else:
    print(f"Failed to update permissions: {test_file}")

print("\nAll tests completed.")