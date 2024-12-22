import csv
import os
from utils.folder_manager import ensure_data_folder_exists
from utils.logger import Logger

class MealController:
    """
    Controller for managing meal plans and grocery lists.

    This class provides functionalities to create, view, and update meal plans
    and generate corresponding grocery lists. It ensures required files exist and
    logs all critical operations.
    """

    def __init__(self):
        """
        Initialize the MealController.

        Ensures the necessary data folders and CSV files (meal_plan.csv, grocery_list.csv) exist.
        """
        self.meal_plan_path = os.path.join(ensure_data_folder_exists(), "meal_plan.csv")
        self.grocery_list_path = os.path.join(ensure_data_folder_exists(), "grocery_list.csv")
        
        # Ensure required CSV files exist with proper headers
        self.create_meal_plan_csv_if_not_exists()
        self.create_grocery_list_csv_if_not_exists()

    def create_meal_plan_csv_if_not_exists(self):
        """
        Create the meal plan CSV file with headers if it doesn't already exist.

        Logs an error if file creation fails.
        """
        if not os.path.exists(self.meal_plan_path):
            try:
                with open(self.meal_plan_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Day", "Meal"])  # Headers for meal plan
                Logger.log_info(f"Created new meal plan CSV file with headers: {self.meal_plan_path}")
            except Exception as e:
                Logger.log_error(f"Error creating meal plan CSV file: {e}")

    def create_grocery_list_csv_if_not_exists(self):
        """
        Create the grocery list CSV file with headers if it doesn't already exist.

        Logs an error if file creation fails.
        """
        if not os.path.exists(self.grocery_list_path):
            try:
                with open(self.grocery_list_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Item"])  # Header for grocery list
                Logger.log_info(f"Created new grocery list CSV file with headers: {self.grocery_list_path}")
            except Exception as e:
                Logger.log_error(f"Error creating grocery list CSV file: {e}")

    def plan_meals(self):
        """
        Prompt the user to plan meals for the week and save them to the meal plan file.

        Logs an error if saving the meal plan fails.
        """
        Logger.log_info("Starting meal planning process.")
        print("\n=== Plan Meals ===")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meal_plan = {}
        for day in days:
            meal = input(f"Enter meal for {day}: ")
            meal_plan[day] = meal
        try:
            with open(self.meal_plan_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Day", "Meal"])  # Re-add headers
                for day, meal in meal_plan.items():
                    writer.writerow([day, meal])
            Logger.log_info("Meal plan saved successfully.")
            print("Meal plan saved successfully!")
        except Exception as e:
            Logger.log_error(f"Error saving meal plan: {e}")

    def view_meal_plan(self):
        """
        Display the current meal plan from the meal plan file.

        Logs an error if reading the meal plan file fails.
        """
        Logger.log_info("Viewing meal plan.")
        print("\n=== View Meal Plan ===")
        if not os.path.exists(self.meal_plan_path):
            Logger.log_warning("No meal plan found.")
            print("No meal plan found.")
            return
        try:
            with open(self.meal_plan_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip headers
                for row in reader:
                    print(f"{row[0]}: {row[1]}")
            Logger.log_info("Displayed meal plan successfully.")
        except Exception as e:
            Logger.log_error(f"Error viewing meal plan: {e}")

    def generate_grocery_list(self):
        """
        Generate a grocery list based on the meal plan and save it to the grocery list file.

        Logs an error if saving the grocery list fails.
        """
        Logger.log_info("Starting grocery list generation process.")
        print("\n=== Generate Grocery List ===")
        if not os.path.exists(self.meal_plan_path):
            Logger.log_warning("No meal plan available to generate grocery list.")
            print("No meal plan available to generate grocery list.")
            return
        grocery_list = []
        try:
            with open(self.meal_plan_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip headers
                for row in reader:
                    ingredients = input(f"Enter ingredients for {row[1]} (comma-separated): ")
                    grocery_list.extend(ingredients.split(","))
            # Remove duplicates and save the grocery list
            grocery_list = list(set(grocery_list))
            with open(self.grocery_list_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Item"])  # Re-add headers
                for item in grocery_list:
                    writer.writerow([item.strip()])
            Logger.log_info("Grocery list generated and saved successfully.")
            print("Grocery list generated and saved!")
        except Exception as e:
            Logger.log_error(f"Error generating grocery list: {e}")
