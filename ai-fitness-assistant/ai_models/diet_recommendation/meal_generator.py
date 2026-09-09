import random


MEAL_DATABASE = {

    # ─────────────────────────────────────────
    #  BREAKFAST  (20 options)
    # ─────────────────────────────────────────
    "breakfast": [
        # Indian
        "Masala omelette (3 eggs) with green chillies & coriander, 2 multigrain rotis, chai",
        "Poha with peanuts, onion, lemon, and coriander, 2 boiled eggs, nimbu pani",
        "Moong dal chilla (3 pieces) with green chutney and low-fat curd",
        "Besan cheela (3 pieces) stuffed with paneer, sliced cucumber, glass of milk",
        "Upma (semolina) with mixed veggies, cashews, curry leaves, 2 boiled eggs",
        "Aloo paratha (2, minimal ghee) with low-fat dahi and pickle",
        "Paneer bhurji with capsicum and tomato, 2 whole wheat rotis, glass of milk",
        "Idli (3 pieces) with sambar and coconut chutney, 2 boiled egg whites",
        "Ragi dosa (2 pieces) with sambar and tomato chutney, boiled egg x2",
        "Oats khichdi with ghee, chia seeds, dry fruits, 2 boiled eggs, banana",
        "Methi paratha (2, minimal oil) with low-fat curd, 1 boiled egg, orange",
        "Sabudana khichdi with peanuts and ghee, banana, glass of milk",
        "Sprouts poha with groundnuts, lemon, green chillies, 2-egg omelette",
        "Dalia (broken wheat) porridge with jaggery and dry fruits, 2 scrambled eggs",
        # Mixed / International
        "Oatmeal with banana, chia seeds, and honey, 2 boiled eggs",
        "Whole wheat toast with peanut butter, banana, and a boiled egg",
        "Greek yogurt with mixed berries, granola, and a drizzle of honey",
        "Scrambled eggs (3) with sautéed spinach and mushrooms, 2 brown bread slices",
        "Smoothie bowl (banana, milk, protein powder) topped with nuts and seeds",
        "Avocado toast on multigrain bread, 2 poached eggs, black coffee",
    ],

    # ─────────────────────────────────────────
    #  LUNCH  (20 options)
    # ─────────────────────────────────────────
    "lunch": [
        # Indian
        "Grilled chicken tikka (200g) with brown rice, dal tadka, cucumber raita",
        "Rajma (1 bowl) with brown rice (150g), grilled paneer (100g), salad",
        "Paneer tikka masala (150g paneer) with 2 rotis, dal, and salad",
        "Fish curry (200g rohu/pomfret) with 150g rice, dal, and sabzi",
        "Tandoori chicken (200g) with mint chutney, 2 rotis, and kachumber salad",
        "Chicken biryani (200g chicken, brown rice) with raita and salad",
        "Chole (1 large bowl) with 2 baked bhature, onion, and green chutney",
        "Dal makhani with 150g brown rice, grilled chicken (150g), salad",
        "Palak paneer (150g paneer) with 2 rotis, salad, and raita",
        "Egg curry (3 eggs) in onion-tomato gravy with 1.5 cups rice and sabzi",
        "Chicken palak (200g) with 2 rotis, moong dal, and curd",
        "Sambar rice (1 medium bowl) with rasam, papad, and 100g grilled fish",
        "Sarson da saag with makki roti (2), boiled chicken (150g), lassi",
        # Mixed / International
        "Grilled chicken (200g) with quinoa, roasted vegetables, and lemon dressing",
        "Tuna salad wrap (whole wheat tortilla, tuna, avocado, spinach, mustard)",
        "Brown rice bowl with grilled salmon (150g), steamed broccoli, soy dressing",
        "Lentil soup (1 bowl) with whole wheat bread, side salad, boiled egg x2",
        "Chicken and vegetable stir-fry with 150g brown rice and sesame sauce",
        "Turkey and avocado sandwich on whole grain bread, side of mixed greens",
        "Baked sweet potato with cottage cheese, black beans, and salsa",
    ],

    # ─────────────────────────────────────────
    #  DINNER  (20 options)
    # ─────────────────────────────────────────
    "dinner": [
        # Indian
        "Grilled surmai/pomfret (200g) with jeera, lemon, dal, jeera aloo, salad",
        "Chicken curry (150g) with 2 whole wheat rotis, sabzi, and curd",
        "Paneer bhurji (150g) with 2 rotis, moong dal soup, stir-fried veggies",
        "Mutton curry (lean, 150g) with 2 rotis, dal, and palak sabzi",
        "Baingan bharta (roasted, minimal oil) with 2 rotis, moong dal, curd",
        "Methi chicken (150g) with 2 rotis, raita, and cucumber salad",
        "Egg masala (3 eggs) with 2 rotis, dal, green salad",
        "Dal palak (1 bowl) with 2 rotis, grilled paneer (100g), salad",
        "Baked tandoori fish (200g) with quinoa pulao (1 cup), raita",
        "Palak paneer (100g paneer, no cream) with 2 rotis, ragi roti, salad",
        "Keema matar (lean, 150g) with 2 whole wheat rotis, raita, salad",
        "Kadhi with 2 rotis and sabzi, side of curd",
        # Mixed / International
        "Baked salmon (150g) with steamed broccoli, sweet potato, lemon butter",
        "Grilled chicken breast (150g) with roasted vegetables and brown rice (100g)",
        "Stir-fried tofu with mixed vegetables, 150g brown rice, soy-ginger sauce",
        "Lean beef / chicken meatballs in tomato sauce with whole wheat pasta",
        "Grilled shrimp with garlic, sautéed spinach, and quinoa",
        "Chicken vegetable soup (clear broth) with 2 whole grain crackers",
        "Baked cod with herb crust, roasted asparagus, mashed sweet potato",
        "Omelette (3 eggs) with feta cheese, tomatoes, spinach, 1 slice toast",
    ],

    # ─────────────────────────────────────────
    #  SNACK  (20 options)
    # ─────────────────────────────────────────
    "snack": [
        # Indian
        "Roasted chana (1 cup) with lemon and black salt, 1 glass buttermilk",
        "Sprouts chaat (moong + chana) with onion, tomato, lemon — 1 bowl",
        "Paneer cubes (100g) with black pepper and lemon, 10 almonds",
        "Sattu sharbat (2 tbsp sattu, lemon, jeera) + 2 boiled eggs",
        "Boiled black chana (1 small bowl) with chaat masala and lemon",
        "Roasted makhana (1 cup) with ghee and himalayan salt",
        "Dahi (low-fat, 1 bowl) with cucumber, mint, and jeera powder",
        "Peanut chikki (2 pieces) + 1 banana + nimbu pani",
        "Murmura (puffed rice) chaat with onion, tomato, lemon — 1 cup",
        "Mixed dry fruits and nuts (almonds, cashews, walnuts — 50g), chaas",
        # Mixed / International
        "Whey protein shake (1 scoop) with milk or water, 1 banana",
        "Greek yogurt (150g) with chia seeds and honey, 10 almonds",
        "Apple slices with peanut butter (2 tbsp), 1 boiled egg",
        "Rice cakes (2) with hummus and cucumber slices",
        "Cottage cheese (100g) with cherry tomatoes and black pepper",
        "Hard-boiled eggs (2) with a pinch of salt and paprika",
        "Banana + almond butter (1 tbsp) + glass of milk",
        "Mixed nuts and seeds trail mix (50g), 1 fruit",
        "Edamame (1 cup, steamed, lightly salted)",
        "Smoothie: spinach + banana + milk + peanut butter (blended)",
    ],
}


def generate_meal_plan(nutrition_targets: dict) -> dict:
    """
    Generate a randomised daily meal plan based on nutrition targets.
    Picks one option per slot from 20 choices each.
    """
    meal_plan = {
        "breakfast": random.choice(MEAL_DATABASE["breakfast"]),
        "lunch":     random.choice(MEAL_DATABASE["lunch"]),
        "dinner":    random.choice(MEAL_DATABASE["dinner"]),
        "snacks":    random.choice(MEAL_DATABASE["snack"]),
        "daily_calorie_target": nutrition_targets["calories"],
    }
    return meal_plan


def generate_weekly_meal_plan(nutrition_targets: dict) -> dict:
    """
    Generate a non-repeating 7-day meal plan based on nutrition targets.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    breakfasts = random.sample(MEAL_DATABASE["breakfast"], 7)
    lunches    = random.sample(MEAL_DATABASE["lunch"],     7)
    dinners    = random.sample(MEAL_DATABASE["dinner"],    7)
    snacks     = random.sample(MEAL_DATABASE["snack"],     7)

    weekly_plan = {}
    for i, day in enumerate(days):
        weekly_plan[day] = {
            "breakfast": breakfasts[i],
            "lunch":     lunches[i],
            "dinner":    dinners[i],
            "snacks":    snacks[i],
        }

    return {
        "daily_calorie_target": nutrition_targets["calories"],
        "week": weekly_plan,
    }