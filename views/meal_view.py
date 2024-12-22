class MealView:
    """
    A class responsible for displaying the meal management menu and the grocery list.

    This class provides methods to show the meal menu options and display the 
    grocery list with item names and their quantities.

    Methods:
        show_meal_menu(): Displays the meal management menu and prompts the user for an option.
        display_grocery_list(grocery_list: dict): Displays the grocery list with items and their quantities.
    """

    def show_meal_menu(self):
        """
        Displays the meal management menu with options for the user to choose from.

        The menu includes options to add a meal, view a meal plan, generate a 
        grocery list, or exit.

        Returns:
            str: The user's choice of the menu option.

        Example:
            meal_view = MealView()
            user_choice = meal_view.show_meal_menu()
        """
        print("\n=== Meal Management ===")
        print("1. Add Meal")
        print("2. View Meal Plan")
        print("3. Generate Grocery List")
        print("4. Exit")
        user_choice = input("Choose an option: ")
        return user_choice

    def display_grocery_list(self, grocery_list):
        """
        Displays the grocery list with item names and their quantities.

        This method iterates over the `grocery_list` dictionary and prints each 
        item along with its count.

        Args:
            grocery_list (dict): A dictionary where keys are item names (str) 
                                  and values are their quantities (int).

        Example:
            grocery_list = {"Tomatoes": 5, "Onions": 2}
            meal_view.display_grocery_list(grocery_list)
        """
        print("\n=== Grocery List ===")
        for item, count in grocery_list.items():
            print(f"{item}: {count}")
