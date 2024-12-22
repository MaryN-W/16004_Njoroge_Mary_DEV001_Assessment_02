class RecipeView:
    """
    A class responsible for handling user interactions related to recipes.

    This class provides methods to get recipe details from the user (such as name, ingredients, and steps), 
    display messages, and show a list of recipes with their details.

    Methods:
        get_recipe_name(new_name=False): Prompts the user to enter a recipe name.
        get_ingredients(new_ingredients=False): Prompts the user to enter ingredients for a recipe.
        get_steps(new_steps=False): Prompts the user to enter the steps for a recipe.
        get_recipe_name_for_edit(): Prompts the user to enter the name of the recipe they wish to edit.
        display_message(message): Displays a message to the user.
        display_recipes(recipes): Displays a list of recipes with their details.
    """

    def get_recipe_name(self, new_name=False):
        """
        Prompts the user to enter the name of a recipe.

        If `new_name` is True, the prompt asks for a new recipe name; otherwise, 
        it asks for an existing recipe name.

        Args:
            new_name (bool): If True, the prompt will ask for a new recipe name. Defaults to False.

        Returns:
            str: The name of the recipe entered by the user.

        Example:
            recipe_name = recipe_view.get_recipe_name(new_name=True)
        """
        prompt = "Enter the new recipe name: " if new_name else "Enter the recipe name: "
        return input(prompt)

    def get_ingredients(self, new_ingredients=False):
        """
        Prompts the user to enter ingredients for a recipe.

        If `new_ingredients` is True, the prompt asks for new ingredients; 
        otherwise, it asks for the existing ingredients.

        Args:
            new_ingredients (bool): If True, the prompt will ask for new ingredients. Defaults to False.

        Returns:
            list: A list of ingredients entered by the user, split by commas.

        Example:
            ingredients = recipe_view.get_ingredients(new_ingredients=True)
        """
        prompt = (
            "Enter new ingredients separated by commas: "
            if new_ingredients
            else "Enter ingredients separated by commas: "
        )
        return input(prompt).split(",")

    def get_steps(self, new_steps=False):
        """
        Prompts the user to enter the steps for a recipe.

        If `new_steps` is True, the prompt asks for updated steps; 
        otherwise, it asks for the initial steps of the recipe.

        Args:
            new_steps (bool): If True, the prompt will ask for updated steps. Defaults to False.

        Returns:
            str: The steps for the recipe entered by the user.

        Example:
            steps = recipe_view.get_steps(new_steps=True)
        """
        prompt = (
            "Enter the updated steps: "
            if new_steps
            else "Enter the steps for this recipe: "
        )
        return input(prompt)

    def get_recipe_name_for_edit(self):
        """
        Prompts the user to enter the name of the recipe they wish to edit.

        Returns:
            str: The name of the recipe to edit.

        Example:
            recipe_name = recipe_view.get_recipe_name_for_edit()
        """
        return input("Enter the name of the recipe you want to edit: ")

    def display_message(self, message):
        """
        Displays a message to the user.

        Args:
            message (str): The message to display.

        Example:
            recipe_view.display_message("Recipe updated successfully.")
        """
        print(message)

    def display_recipes(self, recipes):
        """
        Displays a list of recipes with their details, including name, ingredients, and steps.

        Args:
            recipes (list): A list of recipe objects, where each object has `name`, `ingredients`, and `steps`.

        Example:
            recipes = [recipe1, recipe2]
            recipe_view.display_recipes(recipes)
        """
        print("=== Recipes ===")
        for recipe in recipes:
            print(f"Name: {recipe.name}")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")
            print(f"Steps: {recipe.steps}")
            print("---")
