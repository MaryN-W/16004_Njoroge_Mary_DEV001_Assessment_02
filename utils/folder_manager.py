import os


def ensure_data_folder_exists(folder_name="data"):
    """
    Ensures that the specified data folder exists. If it doesn't, creates it.

    Args:
        folder_name (str): The name of the folder to check or create. Defaults to "data".

    Returns:
        str: The absolute path to the data folder.

    Raises:
        OSError: If there is an error creating the folder.
    """
    try:
        # Get the absolute path of the folder
        folder_path = os.path.abspath(folder_name)
        
        # Check if the folder exists; if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        return folder_path
    except OSError as e:
        print(f"Error ensuring folder exists: {e}")
        raise
