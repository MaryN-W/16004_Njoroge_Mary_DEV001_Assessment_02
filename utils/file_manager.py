import csv
import os


class FileManager:
    """
    A utility class for managing CSV file operations, such as reading, appending, and initializing files.

    Attributes:
        file_path (str): Path to the CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes the FileManager with the path to the CSV file.

        Args:
            file_path (str): Path to the CSV file to be managed.
        """
        self.file_path = file_path

    def read_csv(self):
        """
        Reads the contents of the CSV file and returns it as a list of dictionaries.

        Returns:
            list[dict]: A list of dictionaries representing rows in the CSV file.
                        Returns an empty list if the file doesn't exist or is empty.
        """
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return []  # Return an empty list if the file doesn't exist or is empty

        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return []

    def append_csv(self, data, fieldnames):
        """
        Appends rows of data to the CSV file. If the file doesn't exist or is empty, writes headers first.

        Args:
            data (list[dict]): A list of dictionaries to be written as rows in the CSV file.
            fieldnames (list[str]): A list of strings representing the column headers.
        """
        file_exists = os.path.exists(self.file_path)

        try:
            with open(self.file_path, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists or os.path.getsize(self.file_path) == 0:
                    writer.writeheader()  # Write headers if the file is new or empty
                writer.writerows(data)
        except Exception as e:
            print(f"Error appending to CSV file: {e}")

    def initialize_csv(self, fieldnames):
        """
        Initializes the CSV file by creating or overwriting it with the specified headers.

        Args:
            fieldnames (list[str]): A list of strings representing the column headers.
        """
        try:
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
        except Exception as e:
            print(f"Error initializing CSV file: {e}")
