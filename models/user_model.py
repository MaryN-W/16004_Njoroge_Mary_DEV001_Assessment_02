from utils.file_manager import FileManager

class UserModel:
    """
    Represents the user management model responsible for user registration and validation.

    Attributes:
        file_manager (FileManager): A utility for reading and writing user data to a CSV file.
    """

    def __init__(self):
        """
        Initialize the UserModel with a FileManager instance.
        """
        self.file_manager = FileManager("users.csv")

    def register_user(self, email: str, password: str) -> bool:
        """
        Registers a new user with the provided email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if the user was registered successfully, False if the user already exists.

        Raises:
            ValueError: If the email or password is empty or invalid.
        """
        if not email.strip():
            raise ValueError("Email cannot be empty.")
        if not password.strip():
            raise ValueError("Password cannot be empty.")

        try:
            users = self.file_manager.read_csv()
            for user in users:
                if user.get("email") == email:
                    return False  # User already exists

            # Add the new user to the users.csv file
            self.file_manager.append_csv(
                [{"email": email, "password": password}], ["email", "password"]
            )
            return True
        except Exception as e:
            raise RuntimeError(f"Error during user registration: {e}")

    def validate_user(self, email: str, password: str) -> bool:
        """
        Validates a user's credentials.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if the credentials are valid, False otherwise.

        Raises:
            ValueError: If the email or password is empty or invalid.
        """
        if not email.strip():
            raise ValueError("Email cannot be empty.")
        if not password.strip():
            raise ValueError("Password cannot be empty.")

        try:
            users = self.file_manager.read_csv()
            for user in users:
                if user.get("email") == email and user.get("password") == password:
                    return True
            return False
        except Exception as e:
            raise RuntimeError(f"Error during user validation: {e}")
