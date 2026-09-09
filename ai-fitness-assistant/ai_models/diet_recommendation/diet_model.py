from .calorie_calculator import calculate_calories
from .meal_generator import generate_meal_plan
from .diet_generator import generate_diet_plan


class DietRecommendationModel:

    def __init__(self):
        pass

    def generate_plan(self, weight, height, age, goal, gender="male"):
        """
        Generate complete diet plan
        """

        nutrition = calculate_calories(
            weight_kg=weight,
            height_cm=height,
            age=age,
            goal=goal,
            gender=gender
        )

        meals = generate_meal_plan(nutrition)

        diet = generate_diet_plan(meals, nutrition)

        return {
            "nutrition_targets": nutrition,
            "meal_plan": meals,
            "diet_plan": diet
        }