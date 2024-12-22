from utils.file_manager import FileManager
from collections import defaultdict

class MealModel:
    """
    A model for managing meal plans, including functionality for loading, viewing, adding meals,
    saving meal plans, and generating grocery lists.
    """

    def __init__(self):
        """
        Initializes the MealModel instance and loads the existing meal plan from a CSV file.
        """
        self.file_manager = FileManager("meal_plan.csv")
        self.meal_plan = self.load_meal_plan()

    def load_meal_plan(self):
        """
        Load the meal plan from the CSV file and organize it into a dictionary.

        Returns:
            defaultdict: A dictionary where keys are days of the week and values are lists of meals with ingredients.
        """
        meal_plan = defaultdict(list)
        try:
            data = self.file_manager.read_csv()
            for row in data:
                day = row.get("day", "Unknown")
                meal = row.get("meal", "Unknown")
                ingredients = row.get("ingredients", "").split(", ")
                meal_plan[day].append((meal, ingredients))
        except Exception as e:
            print(f"Error loading meal plan: {e}")
        return meal_plan

    def get_meal_plan(self):
        """
        Retrieve the current meal plan.

        Returns:
            defaultdict: The current meal plan dictionary.
        """
        return self.meal_plan

    def add_meal(self):
        """
        Prompt the user to add a new meal to the meal plan and save the changes.
        """
        try:
            day = input("Enter the day of the week (e.g., Monday): ").strip().capitalize()
            meal = input("Enter the meal name: ").strip()
            ingredients = input("Enter the ingredients (comma separated): ").strip()

            if not day or not meal or not ingredients:
                print("All fields are required. Please try again.")
                return

            ingredients_list = ingredients.split(", ")
            self.meal_plan[day].append((meal, ingredients_list))
            self.save_meal_plan()
            print("Meal added successfully!")
        except Exception as e:
            print(f"Error adding meal: {e}")

    def view_meal_plan(self):
        """
        Display the current meal plan in a user-friendly format.
        """
        print("\n=== Your Meal Plan ===")
        if not self.meal_plan:
            print("No meals found in the meal plan.")
            return

        for day, meals in self.meal_plan.items():
            print(f"\n{day}:")
            for meal, ingredients in meals:
                print(f"  {meal} - Ingredients: {', '.join(ingredients)}")

    def save_meal_plan(self):
        """
        Save the current meal plan to the CSV file.
        """
        fieldnames = ["day", "meal", "ingredients"]
        data = []
        for day, meals in self.meal_plan.items():
            for meal, ingredients in meals:
                data.append({
                    "day": day,
                    "meal": meal,
                    "ingredients": ", ".join(ingredients)
                })
        try:
            self.file_manager.write_csv(data, fieldnames)
            print("Meal plan saved successfully!")
        except Exception as e:
            print(f"Error saving meal plan: {e}")

    def generate_grocery_list(self):
        """
        Generate a grocery list based on the current meal plan.

        Returns:
            dict: A dictionary where keys are ingredients and values are their quantities.
        """
        grocery_list = defaultdict(int)
        for meals in self.meal_plan.values():
            for _, ingredients in meals:
                for ingredient in ingredients:
                    grocery_list[ingredient] += 1

        if not grocery_list:
            print("No ingredients found in the meal plan.")
            return {}

        print("\n=== Grocery List ===")
        for ingredient, quantity in grocery_list.items():
            print(f"{ingredient}: {quantity}")
        return grocery_list
