def calculate_calories(weight_kg: float, height_cm: float, goal: str, age: int = 25, gender: str = "male") -> dict:
    """
    Calculate TDEE and macros using Mifflin-St Jeor Equation.
    Defaulting to moderate activity multiplier (1.55).
    """
    # BMR calculation
    if gender.lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    tdee = bmr * 1.55 # moderate activity

    # Adjust based on goal
    if goal == "muscle_gain":
        target_calories = int(tdee + 500)
        protein_g = int(weight_kg * 2.2) # High protein
    elif goal == "fat_loss":
        target_calories = int(tdee - 500)
        protein_g = int(weight_kg * 2.0)
    elif goal == "endurance":
        target_calories = int(tdee + 200)
        protein_g = int(weight_kg * 1.6)
    else: # maintenance
        target_calories = int(tdee)
        protein_g = int(weight_kg * 1.8)

    # Remaining calories for carbs and fats
    protein_cals = protein_g * 4
    remaining_cals = target_calories - protein_cals

    if goal == "fat_loss":
        fat_g = int((remaining_cals * 0.4) / 9)
        carb_g = int((remaining_cals * 0.6) / 4)
    else:
        fat_g = int((target_calories * 0.25) / 9)
        carb_g = int((target_calories - protein_cals - (fat_g * 9)) / 4)

    return {
        "calories": target_calories,
        "protein": f"{protein_g}g",
        "carbs": f"{carb_g}g",
        "fats": f"{fat_g}g"
    }
