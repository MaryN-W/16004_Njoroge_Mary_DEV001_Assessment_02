class Recipe:
    """
    Represents a recipe with a name, ingredients, and preparation steps.

    Attributes:
        name (str): The name of the recipe.
        ingredients (list): A list of ingredients required for the recipe.
        steps (str): The preparation steps for the recipe.
    """

    def __init__(self, name: str, ingredients: list, steps: str):
        """
        Initialize a Recipe instance.

        Args:
            name (str): The name of the recipe.
            ingredients (list): A list of ingredients required for the recipe.
            steps (str): The preparation steps for the recipe.
        """
        if not name.strip():
            raise ValueError("Recipe name cannot be empty.")
        if not ingredients:
            raise ValueError("Ingredients list cannot be empty.")
        if not steps.strip():
            raise ValueError("Preparation steps cannot be empty.")

        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def to_dict(self):
        """
        Converts the Recipe instance to a dictionary.

        Returns:
            dict: A dictionary representation of the recipe.
        """
        return {
            "name": self.name,
            "ingredients": ",".join(self.ingredients),
            "steps": self.steps,
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Creates a Recipe instance from a dictionary.

        Args:
            data (dict): A dictionary with keys "name", "ingredients", and "steps".

        Returns:
            Recipe: A Recipe instance created from the dictionary.

        Raises:
            KeyError: If any of the required keys are missing from the dictionary.
            ValueError: If the dictionary contains invalid or empty values.
        """
        try:
            name = data["name"]
            ingredients = data["ingredients"].split(",") if data["ingredients"] else []
            steps = data["steps"]

            return Recipe(name=name, ingredients=ingredients, steps=steps)
        except KeyError as e:
            raise KeyError(f"Missing required key: {e}")
        except Exception as e:
            raise ValueError(f"Invalid data provided: {e}")
