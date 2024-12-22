import csv
import os
from utils.folder_manager import ensure_data_folder_exists
from utils.logger import Logger

class RecipeController:
    """
    A controller for managing recipe-related operations such as adding, viewing, editing, 
    and deleting recipes. Recipes are stored in a CSV file.
    """

    def __init__(self):
        """
        Initialize the RecipeController by setting up the file path for recipes and ensuring 
        the CSV file exists with appropriate headers.
        """
        self.file_path = os.path.join(ensure_data_folder_exists(), "recipes.csv")
        self.create_recipes_csv_if_not_exists()

    def create_recipes_csv_if_not_exists(self):
        """
        Create the recipes CSV file with headers if it doesn't already exist.
        """
        if not os.path.exists(self.file_path):
            try:
                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Recipe Name", "Ingredients"])  # Headers for recipes
                Logger.log_info(f"Created new recipes CSV file with headers: {self.file_path}")
            except Exception as e:
                Logger.log_error(f"Error creating recipes CSV file: {e}")
                print(f"An error occurred while creating the recipes CSV file: {e}")

    def add_recipe(self):
        """
        Prompt the user to add a new recipe and append it to the CSV file.
        """
        print("\n=== Add Recipe ===")
        recipe_name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma-separated): ")
        try:
            with open(self.file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([recipe_name, ingredients])
            Logger.log_info(f"Added recipe: {recipe_name}")
            print("Recipe added successfully!")
        except Exception as e:
            Logger.log_error(f"Error adding recipe: {e}")
            print(f"An error occurred while adding the recipe: {e}")

    def view_recipes(self):
        """
        Display all recipes from the CSV file with their ingredients.
        """
        print("\n=== View Recipes ===")
        if not os.path.exists(self.file_path):
            print("No recipes found.")
            Logger.log_warning("Attempted to view recipes but no recipes file exists.")
            return
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)
                for idx, row in enumerate(reader, start=1):
                    print(f"{idx}. {row[0]} - Ingredients: {row[1]}")
        except Exception as e:
            Logger.log_error(f"Error viewing recipes: {e}")
            print(f"An error occurred while viewing the recipes: {e}")

    def edit_recipe(self):
        """
        Allow the user to edit an existing recipe by selecting it from a list of recipes.
        """
        print("\n=== Edit Recipe ===")
        if not os.path.exists(self.file_path):
            print("No recipes to edit.")
            Logger.log_warning("Attempted to edit recipes but no recipes file exists.")
            return
        try:
            with open(self.file_path, mode="r") as file:
                recipes = list(csv.reader(file))

            if not recipes:
                print("No recipes found.")
                Logger.log_warning("No recipes found in the file during editing attempt.")
                return

            # Skip the header row
            recipes = recipes[1:]

            self.view_recipes()
            choice = int(input("Choose a recipe number to edit: ")) - 1
            if 0 <= choice < len(recipes):
                new_name = input("Enter new recipe name: ")
                new_ingredients = input("Enter new ingredients (comma-separated): ")
                recipes[choice] = [new_name, new_ingredients]
            
                # Reinsert the header row
                recipes.insert(0, ["Recipe Name", "Ingredients"])

                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(recipes)
                Logger.log_info(f"Updated recipe: {new_name}")
                print("Recipe updated successfully!")
            else:
                print("Invalid choice.")
                Logger.log_warning(f"Invalid choice during recipe edit: {choice + 1}")
        except Exception as e:
            Logger.log_error(f"Error editing recipe: {e}")
            print(f"An error occurred while editing the recipe: {e}")


    def delete_recipe(self):
        """
        Allow the user to delete a recipe by selecting it from a list of recipes.
        """
        print("\n=== Delete Recipe ===")
        if not os.path.exists(self.file_path):
            print("No recipes to delete.")
            Logger.log_warning("Attempted to delete recipes but no recipes file exists.")
            return

        try:
            with open(self.file_path, mode="r") as file:
                recipes = list(csv.reader(file))

            if not recipes:
                print("No recipes found.")
                Logger.log_warning("No recipes found in the file during deletion attempt.")
                return

            # Skip the header row
            recipes = recipes[1:]

            self.view_recipes()
            choice = int(input("Choose a recipe number to delete: ")) - 1
            if 0 <= choice < len(recipes):
                deleted_recipe = recipes.pop(choice)
            
                # Reinsert the header row
                recipes.insert(0, ["Recipe Name", "Ingredients"])

                with open(self.file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(recipes)
                Logger.log_info(f"Deleted recipe: {deleted_recipe[0]}")
                print(f"Recipe '{deleted_recipe[0]}' deleted successfully!")
            else:
                print("Invalid choice.")
                Logger.log_warning(f"Invalid choice during recipe deletion: {choice + 1}")
        except Exception as e:
            Logger.log_error(f"Error deleting recipe: {e}")
            print(f"An error occurred while deleting the recipe: {e}")
