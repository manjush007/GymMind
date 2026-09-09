import pytest
from ai_models.diet_recommendation.calorie_calculator import calculate_calories
from ai_models.diet_recommendation.diet_generator import generate_diet_plan

def test_calorie_calculator_muscle_gain():
    res = calculate_calories(weight_kg=80, height_cm=180, goal="muscle_gain", age=30)
    assert res["calories"] > 2500 # Should be high for muscle gain
    assert "g" in res["protein"]
    assert "g" in res["carbs"]
    assert "g" in res["fats"]

def test_calorie_calculator_fat_loss():
    res = calculate_calories(weight_kg=80, height_cm=180, goal="fat_loss", age=30)
    assert res["calories"] < 2500 # Should be lower for fat loss

def test_diet_generator():
    res = generate_diet_plan(weight=75, height=175, goal="muscle_gain")
    assert res["goal"] == "muscle_gain"
    assert "calories" in res
    assert len(res["meals"]) >= 3
    assert "eggs" in res["meals"][0].lower() # From our mock DB
