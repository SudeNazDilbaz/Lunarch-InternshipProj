from secure_uploader.uploader import secure_upload


def main():
    result = secure_upload(
        "tests/sample_files/sample.jpg",
        "my photo.jpg",
        "uploads",
    )

    print(result)


if __name__ == "__main__":
    main()