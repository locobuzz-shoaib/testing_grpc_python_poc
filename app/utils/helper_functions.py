import os


def custom_normpath(path: str) -> str:
    # Normalize the path
    normalized_path = os.path.normpath(path)
    # Replace forward slashes with backslashes for consistency
    return normalized_path.replace('/', '\\')
