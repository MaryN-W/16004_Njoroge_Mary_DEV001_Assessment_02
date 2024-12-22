class UserView:
    """
    A class responsible for displaying user-related menu options and messages.

    This class provides methods to show the user menu, display a welcome message 
    upon successful login, and handle user interactions.

    Methods:
        show_user_menu(): Displays the user menu with options to register, login, or exit.
        show_welcome_message(email): Displays a welcome message with the user's email address.
    """

    def show_user_menu(self):
        """
        Displays the user menu with options for the user to choose from.

        The menu includes options to register, login, or exit.

        Returns:
            str: The user's choice from the menu.

        Example:
            user_choice = user_view.show_user_menu()
        """
        print("\nUser Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        user_choice = input("Enter your choice: ")
        return user_choice

    def show_welcome_message(self, email):
        """
        Displays a welcome message to the user with their email address.

        This method is typically called after a user logs in successfully.

        Args:
            email (str): The email address of the logged-in user.

        Example:
            user_view.show_welcome_message("user@example.com")
        """
        print(f"\nWelcome back, {email}!")
