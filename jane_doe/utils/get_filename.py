import os

def get_filename(file_path: str) -> str:
    """
    Retrieve the file name from a given file path.

    Args:
        file_path (str): The full file path as a string.

    Returns:
        str: The file name extracted from the path.
    """
    # Use os.path.basename to extract the file name
    return os.path.basename(file_path)