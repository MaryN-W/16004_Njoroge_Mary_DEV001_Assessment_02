import csv
import os
import bcrypt
from utils.logger import Logger
from models.user_model import UserModel


class AuthManager:
    """
    Manages user authentication, including registration and login.

    Attributes:
        user_model (UserModel): The user model for handling user data.
        current_user (str): The email of the currently logged-in user.
        user_file_path (str): Path to the CSV file storing user credentials.
    """

    def __init__(self):
        """
        Initializes the AuthManager with necessary attributes and ensures the user CSV file exists.
        """
        self.user_model = UserModel()
        self.current_user = None  # Initialize current_user as None
        self.user_file_path = "data/users.csv"  # Path to the user CSV file
        self.create_user_csv_if_not_exists()

    def create_user_csv_if_not_exists(self):
        """
        Ensures the user CSV file exists. Creates it with headers if it doesn't.
        """
        if not os.path.exists(self.user_file_path):
            try:
                with open(self.user_file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Email", "Password"])  # Writing the headers
                Logger.log_info(f"Created new user CSV file with headers: {self.user_file_path}")
            except Exception as e:
                error_message = f"An error occurred while creating the users CSV file: {e}"
                print(error_message)
                Logger.log_error(error_message)

    def register_user(self):
        """
        Registers a new user by prompting for email and password.
        Validates the email for uniqueness and securely hashes the password before storing.

        Raises:
            ValueError: If email or password input is invalid.
        """
        email = input("Enter your email: ").strip()
        password = input("Enter a password: ").strip()

        if not email or not password:
            raise ValueError("Email and password must not be empty.")

        try:
            # Check if the email already exists
            with open(self.user_file_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                if any(row["Email"] == email for row in reader):
                    print("Email already registered. Please try again with a different email.")
                    return

            # Hash the password and save the user
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            with open(self.user_file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([email, hashed_password.decode('utf-8')])
            print("User registered successfully!")
            Logger.log_info(f"User registered: {email}")

        except Exception as e:
            error_message = f"An error occurred during registration: {e}"
            print(error_message)
            Logger.log_error(error_message)

    def login_user(self):
        """
        Logs in a user by verifying the email and password.
        If successful, sets the current user to the logged-in user's email.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        if not email or not password:
            print("Email and password must not be empty.")
            return False

        try:
            # Check credentials
            with open(self.user_file_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Email"] == email:
                        stored_hashed_password = row["Password"]
                        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                            self.current_user = email
                            print(f"Login successful! Welcome, {self.current_user}")
                            Logger.log_info(f"User logged in successfully: {email}")
                            return True

            # No match found
            print("Invalid email or password. Please try again.")
            Logger.log_warning(f"Failed login attempt for email: {email}")
            return False

        except Exception as e:
            error_message = f"An error occurred during login: {e}"
            print(error_message)
            Logger.log_error(error_message)
            return False
