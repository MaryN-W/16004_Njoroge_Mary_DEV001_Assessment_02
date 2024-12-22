from views.user_view import UserView
from utils.auth_manager import AuthManager
from controllers.meal_controller import MealController
from controllers.recipe_controller import RecipeController

class UserController:
    """
    A controller to manage user interactions including authentication, meal planning,
    and recipe management.
    """

    def __init__(self):
        """
        Initialize the UserController with instances of UserView, AuthManager,
        MealController, and RecipeController.
        """
        self.user_view = UserView()
        self.auth_manager = AuthManager()
        self.meal_controller = MealController()
        self.recipe_controller = RecipeController()

    def start(self):
        """
        Start the application and display the main user menu for registration,
        login, or exit options.
        """
        while True:
            choice = self.user_view.show_user_menu()
            if choice == "1":  # Register user
                self.auth_manager.register_user()
            elif choice == "2":  # Login user
                if self.auth_manager.login_user():
                    self.logged_in_menu()
                else:
                    print("Login failed. Please try again.")
            elif choice == "3":  # Exit
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

    def logged_in_menu(self):
        """
        Display the main menu after a successful login, allowing users
        to plan meals, view meal plans, generate grocery lists, or manage recipes.
        """
        while True:
            print("\n=== Main Menu ===")
            print("1. Plan Meals")
            print("2. View Meal Plan")
            print("3. Generate Grocery List")
            print("4. Manage Recipes")
            print("5. Logout")
            choice = input("Choose an option: ")
            if choice == "1":
                self.meal_controller.plan_meals()
            elif choice == "2":
                self.meal_controller.view_meal_plan()
            elif choice == "3":
                self.meal_controller.generate_grocery_list()
            elif choice == "4":
                self.manage_recipes()
            elif choice == "5":
                print("Logged out successfully!")
                break
            else:
                print("Invalid option, please try again.")

    def manage_recipes(self):
        """
        Display the recipe management menu, allowing users to add, view,
        edit, or delete recipes, or return to the main menu.
        """
        while True:
            print("\n=== Recipe Menu ===")
            print("1. Add Recipe")
            print("2. View Recipes")
            print("3. Edit Recipe")
            print("4. Delete Recipe")
            print("5. Back to Main Menu")
            choice = input("Choose an option: ")
            if choice == "1":
                self.recipe_controller.add_recipe()
            elif choice == "2":
                self.recipe_controller.view_recipes()
            elif choice == "3":
                self.recipe_controller.edit_recipe()
            elif choice == "4":
                self.recipe_controller.delete_recipe()
            elif choice == "5":
                break
            else:
                print("Invalid option, please try again.")
