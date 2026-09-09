from .calorie_calculator import calculate_calories
import random

# ─────────────────────────────────────────────
#  INDIAN DIET DATABASE  (ai_fit agent)
#  Structure: goal → meal_slot → [options]
#  Each slot has 10+ options for variety/rotation
# ─────────────────────────────────────────────

INDIAN_MEALS_DB = {

    # ══════════════════════════════════════════
    #  MUSCLE GAIN  (~high protein, mod carbs)
    # ══════════════════════════════════════════
    "muscle_gain": {
        "breakfast": [
            "6 egg whites + 1 yolk bhurji with onion-tomato masala, 2 multigrain rotis, 1 banana",
            "Paneer bhurji (150g paneer) with capsicum & tomato, 2 whole wheat parathas, glass of full-fat milk",
            "Masala omelette (4 eggs) with green chillies & coriander, 2 slices brown bread, 1 orange",
            "Boiled egg chaat (5 eggs) with onion, tomato, chaat masala, 1 bowl poha with peanuts",
            "Moong dal chilla (4 pieces) stuffed with paneer, green chutney, 1 glass protein lassi",
            "Besan cheela (3 pieces) with paneer filling, 1 bowl curd, 2 boiled eggs on the side",
            "Chicken keema paratha (2 parathas), 1 bowl dahi, sliced cucumber",
            "Doodh dalia (milk daliya with dry fruits), 3 boiled eggs, 1 apple",
            "Sabudana khichdi with peanuts and ghee, 4 scrambled eggs, 1 glass milk",
            "Oats upma with 2 eggs on top, mixed veggies, 1 bowl curd, 1 banana",
            "Sprouts poha with groundnuts & lemon, 4-egg omelette, 1 glass whey shake",
            "Thepla (3 pieces) with methi-paneer stuffing, 1 bowl dahi, handful of almonds",
        ],
        "lunch": [
            "200g grilled chicken tikka, 150g brown rice, dal tadka, cucumber raita, 1 roti",
            "Mutton keema (lean, 200g) with peas, 2 rotis, palak dal, curd",
            "Egg curry (4 eggs) in onion-tomato gravy, 150g white rice, papad, salad",
            "Chicken biryani (200g chicken, brown rice), raita, salad",
            "Rajma (1 bowl) + 150g brown rice, grilled paneer 100g, salad",
            "Fish curry (200g rohu/pomfret) in mustard gravy, 150g rice, dal, sabzi",
            "Tandoori chicken (200g) with mint chutney, 2 rotis, dal makhani (small), salad",
            "Chicken palak (200g) with 2 rotis, moong dal, 1 bowl curd",
            "Chole (1 large bowl) + 2 bhature (baked), grilled chicken 150g on side",
            "Paneer tikka masala (200g paneer), 150g rice, dal, salad",
            "Mutton rogan josh (200g lean), 2 rotis, dal, raita",
            "Sarson da saag with makki roti (2), 150g boiled chicken, glass of lassi",
        ],
        "snack": [
            "1 scoop whey protein shake + 1 banana + handful of roasted chana",
            "Paneer cubes (100g) with black pepper and lemon, 10 almonds, 5 walnuts",
            "Roasted makhana (fox nuts) 1 cup, 1 boiled egg, 1 glass milk",
            "Sprouts chaat (moong + chana) with onion, tomato, lemon — 1 large bowl",
            "Sattu sharbat (2 tbsp sattu in water with lemon & jeera), boiled egg x2",
            "Peanut butter (2 tbsp) on 2 multigrain crackers, 1 banana, whey shake",
            "Boiled black chana chaat (1 bowl), 1 glass buttermilk, handful almonds",
            "Greek yogurt (150g) with chia seeds and honey, 10 cashews",
            "Masala mixed nuts (almonds, cashews, walnuts — 50g), 1 glass protein lassi",
            "Egg white omelette wrap (3 whites) with paneer and veggies, green chutney",
            "Dahi with flaxseeds and a drizzle of honey (1 bowl), 2 boiled eggs",
            "Chana jor garam (roasted, 1 cup) + nimbu pani with black salt",
        ],
        "dinner": [
            "200g lean mutton curry, 2 rotis, palak sabzi, 1 bowl curd",
            "Grilled fish (surmai/pomfret, 200g) with haldi-pepper, dal, 1 roti, sabzi",
            "Chicken curry (200g) with 1.5 cups brown rice, salad, raita",
            "Paneer bhurji (150g) with 2 rotis, moong dal soup, stir-fried veggies",
            "Egg masala (4 eggs) with 2 rotis, dal, sabzi, curd",
            "Keema matar (lean 200g) with 2 whole wheat rotis, raita, salad",
            "Lentil soup (mixed dal) + 2 rotis + grilled chicken 150g",
            "Palak paneer (150g paneer) + 2 rotis + brown rice 100g + salad",
            "Grilled prawn masala (200g) with 1 cup rice, dal, sabzi",
            "Chicken do pyaza (200g) with 2 rotis, sabzi, dahi",
            "Baked tandoori fish (200g) + quinoa pulao 1 cup + raita",
            "Mutton shami kebab (3 pieces) with 2 rotis, dal, green salad",
        ],
    },

    # ══════════════════════════════════════════
    #  FAT LOSS  (~high protein, low carb/fat)
    # ══════════════════════════════════════════
    "fat_loss": {
        "breakfast": [
            "3 egg whites + 1 whole egg omelette with sautéed methi and spinach, green tea",
            "Moong dal chilla (2 pieces, no oil), green chutney, 1 bowl fruit (papaya/watermelon)",
            "Besan chilla (2 pieces) with tomato-onion stuffing, 1 glass nimbu pani (no sugar)",
            "Vegetable oats upma (no ghee) with 2 boiled eggs, black coffee",
            "Poha (light, 1 small bowl) with lots of veggies and lemon, 2 boiled egg whites",
            "Dahi (low fat, 1 cup) with cucumber and mint, 2 egg whites scrambled",
            "Sprouts salad (moong, 1 bowl) with lemon and salt, 2 boiled eggs",
            "Ragi dosa (2 pieces, minimal oil) with sambar, 1 glass buttermilk",
            "Idli (2 pieces) with sambar and green chutney, 2 boiled egg whites",
            "Vegetable daliya (1 small bowl) with methi and jeera, black tea",
            "Egg white bhurji (5 whites) with capsicum and onion, 1 slice brown bread",
            "Lauki ka paratha (1, minimal oil) with low-fat curd, cucumber salad",
        ],
        "lunch": [
            "150g grilled chicken breast, large kachumber salad, 1 small bowl moong dal, 1 roti",
            "Tandoori fish (150g) with mint chutney, dal soup, mixed greens salad",
            "Chicken salad bowl (150g grilled chicken, cucumber, tomato, onion, lemon dressing)",
            "Palak dal (1 bowl) + 1 roti + 100g grilled paneer, green salad",
            "Mixed vegetable sabzi + 1 roti + moong dal + low-fat curd",
            "Grilled pomfret (150g) with jeera, lemon, dal, stir-fried veggies, no rice",
            "Baingan bharta (roasted, no excess oil) + 2 rotis + dal + salad",
            "Chicken soup (clear) + 1 roti + green salad + 2 boiled eggs",
            "Rajma (small bowl) + brown rice (small portion, 100g) + salad + raita",
            "Kadhi (low-fat) + 1 roti + sabzi + cucumber raita",
            "Egg curry (2 eggs) in light tomato gravy, 1 roti, dal, large salad",
            "Stir-fried chicken with Indian spices, 100g brown rice, dal, sabzi",
        ],
        "snack": [
            "1 bowl low-fat dahi with jeera powder and black salt, 1 small bowl sprouts",
            "Cucumber, carrot, and radish sticks with green chutney dip",
            "1 glass thin buttermilk (chaas) with ginger and curry leaves, handful roasted chana",
            "Boiled black chana (small bowl) with lemon and salt",
            "1 apple or guava, 2 boiled egg whites",
            "Nimbu pani (no sugar, black salt), roasted makhana (small cup)",
            "Tomato soup (homemade, no cream), 1 boiled egg",
            "Watermelon cubes (1 cup), 1 boiled egg white",
            "Moong sprouts chaat (no fried items), green chutney",
            "Jaljeera drink, 10 almonds, 1 small bowl dahi",
            "Grilled paneer cubes (50g, low fat), cucumber slices, green tea",
            "Papaya chaat (1 bowl) with chaat masala and lemon",
        ],
        "dinner": [
            "150g baked fish (rohu/surmai) with haldi-pepper-lemon, stir-fried bhindi, 1 small bowl dal",
            "Grilled chicken tikka (150g), palak sabzi (no cream), 1 small roti, salad",
            "Egg white curry (4 whites) in light gravy, 1 roti, green salad",
            "Dal palak soup (1 bowl) + grilled paneer (100g) + 1 small roti",
            "Baked tandoori chicken (150g) + roasted vegetables + raita",
            "Fish tikka (150g) + stir-fried veggies + 1 small bowl daliya",
            "Lauki dal (bottle gourd) + 1 roti + salad + low-fat curd",
            "Chicken clear soup + vegetable sabzi + 1 small roti",
            "Methi chicken (150g, minimal oil) + 1 roti + cucumber salad",
            "Steamed pomfret with Indian spices + moong dal + sabzi",
            "Paneer tikka (100g, grilled) + 1 roti + dal + salad",
            "Ragi roti (1) + palak paneer (100g paneer, no cream) + salad",
        ],
    },

    # ══════════════════════════════════════════
    #  ENDURANCE  (~high carb, mod protein)
    # ══════════════════════════════════════════
    "endurance": {
        "breakfast": [
            "Large bowl oats khichdi with ghee, chia seeds, 2 boiled eggs, 1 banana",
            "Sabudana khichdi (large) with peanuts and ghee, 1 banana, glass of milk",
            "Poha (large, with peanuts) + 2 eggs + glass of milk with turmeric",
            "Banana peanut butter shake (2 bananas, 2 tbsp PB, milk) + 2 egg omelette",
            "Upma (semolina, large bowl) with cashews and curry leaves, 2 boiled eggs, fruit",
            "Idli (4 pieces) with sambar and coconut chutney, 2 eggs, glass of milk",
            "Whole wheat paratha (2) with ghee + banana + glass of milk",
            "Dalia (broken wheat porridge) with jaggery and ghee, dry fruits, 2 eggs",
            "Rice poha (large) with groundnuts, lemon, green chillies, boiled egg x2",
            "Ragi porridge (1 large bowl) with honey and nuts, 2 scrambled eggs",
            "Rava dosa (2) with sambar + coconut chutney, 2 boiled eggs, banana",
            "Sweet potato boiled (150g) + 2 eggs bhurji + 1 glass milk + dates x3",
        ],
        "lunch": [
            "Chicken biryani (large, brown rice 200g, 200g chicken) + raita + salad",
            "Rajma chawal (large bowl rajma + 200g rice) + grilled chicken 150g + raita",
            "Roti roll (3 rotis) with grilled chicken, green chutney, onion + chole (1 bowl)",
            "Dal makhani + 200g brown rice + tandoori chicken 150g + salad",
            "Chole bhature (2 baked bhature) + chole (large) + raita + green chutney",
            "Mutton pulao (200g) + raita + dal + salad",
            "Paneer butter masala + 200g rice + 2 rotis + salad",
            "Fish curry (200g) + 200g white rice + dal + papad",
            "Chicken curry (200g) + 3 rotis + sabzi + raita",
            "Aloo matar + 200g rice + dal + grilled protein 100g",
            "Mixed dal khichdi (large, with ghee) + kadhi + papad + chicken 150g",
            "Egg curry (4 eggs) + 200g rice + 2 rotis + dahi",
        ],
        "snack": [
            "2 bananas + peanut butter (2 tbsp) + 1 glass nimbu pani with sugar and salt",
            "Dates (6) + mixed nuts (30g) + 1 glass milk",
            "Sweet potato chaat (1 bowl boiled sweet potato, lemon, chaat masala)",
            "Banana shake (2 bananas, milk, honey) + handful of roasted chana",
            "Groundnut chikki (2 pieces) + 1 banana + 1 glass lassi",
            "Poha chivda (1 cup) + 1 banana + nimbu pani",
            "Khajur (dates) milkshake + handful almonds and cashews",
            "Mango lassi (1 glass, during season) + roasted chana (1 cup)",
            "Sattu sharbat (3 tbsp sattu, jaggery, lemon) + boiled egg x2",
            "Roti with jaggery and ghee (1 roti) + glass of milk",
            "Energy balls (oats + peanut butter + jaggery + sesame, 3 balls) + milk",
            "Corn chaat (boiled corn, lemon, butter, masala, 1 cup) + buttermilk",
        ],
        "dinner": [
            "Whole wheat pasta with lean chicken keema and tomato-masala sauce, side salad",
            "Egg fried rice (brown rice, 3 eggs, veggies) + chicken 150g + raita",
            "Chicken pulao (200g rice, 150g chicken) + dal + raita",
            "Dal khichdi (large) with ghee + grilled fish 150g + sabzi",
            "Paneer bhurji + 2 rotis + rice kheer (small) + salad",
            "Aloo gobhi sabzi + 2 rotis + dal + dahi",
            "Chicken stew (Indian spices, potatoes, carrots) + 2 rotis",
            "Mutton soup (bone broth) + 2 rotis + sabzi",
            "Mixed vegetable pulao (large) + dal makhani + raita",
            "Fish curry + 200g rice + dal + papad",
            "Rajma + 2 rotis + rice 100g + raita + salad",
            "Egg biryani (3 eggs, brown rice 200g) + raita + salad",
        ],
    },

    # ══════════════════════════════════════════
    #  MAINTENANCE  (~balanced macros)
    # ══════════════════════════════════════════
    "maintenance": {
        "breakfast": [
            "2 eggs bhurji with onion-tomato, 1 bowl upma with mixed veggies, 1 glass lassi",
            "Aloo paratha (2) with low-fat curd and pickle, 1 boiled egg, chai",
            "Idli (3) + sambar + coconut chutney + boiled egg x2",
            "Poha (medium bowl) with peanuts and coriander, 2 scrambled eggs, tea",
            "Whole wheat toast (2 slices) with paneer spread, 2 eggs, 1 banana",
            "Moong dal chilla (3) with green chutney, 1 bowl curd, fruit",
            "Ragi dosa (2) with sambar and chutney, 2 boiled eggs, coffee",
            "Oats with milk, topped with banana and nuts, 2 boiled eggs",
            "Methi paratha (2, minimal ghee) with curd, 1 boiled egg, orange",
            "Besan cheela (2) + dahi + 1 boiled egg + 1 glass milk",
            "Puri (2, small) with aloo sabzi + 2 boiled eggs + lassi (small)",
            "Doodh poha (milk poha) with dry fruits + 2 egg whites omelette",
        ],
        "lunch": [
            "Chicken or paneer burrito bowl (brown rice, rajma, green chutney, salsa, curd)",
            "Dal fry + 2 rotis + sabzi + 100g grilled chicken + salad",
            "Chole + 1 roti + brown rice 100g + raita + salad",
            "Fish curry + 150g rice + dal + papad + salad",
            "Paneer tikka masala (100g) + 2 rotis + salad + raita",
            "Egg curry (3 eggs) + 150g rice + sabzi + dahi",
            "Rajma + brown rice (150g) + raita + salad",
            "Butter chicken (150g, light gravy) + 2 rotis + dal + salad",
            "Vegetable biryani (150g) + grilled chicken 150g + raita",
            "Dal makhani + 2 rotis + 100g rice + salad + curd",
            "Mixed veg korma + 2 rotis + rice 100g + raita",
            "Sambar rice (medium bowl) + rasam + papad + 100g grilled fish",
        ],
        "snack": [
            "Protein shake with milk, mixed fruit chaat with chaat masala",
            "Masala chai + 2 digestive biscuits + handful of mixed nuts",
            "Curd with honey and granola (Indian style with murmura), 1 fruit",
            "Roasted makhana (1 cup) + 1 glass chaas",
            "Peanut chikki (1-2 pieces) + nimbu pani",
            "Bread pakora (1, baked) + green chutney + chai",
            "Fruit bowl (apple, banana, papaya) with chaat masala",
            "Boiled egg (1) + roasted chana (handful) + buttermilk",
            "Namkeen mixture (small bowl, light) + green tea",
            "Smoothie (mango/banana + milk + honey)",
            "Mathri (2 pieces) with dahi + 1 boiled egg",
            "Murmura (puffed rice) chaat with onion, tomato, lemon — 1 cup",
        ],
        "dinner": [
            "Grilled surmai or rohu, jeera aloo (small), dal soup, green salad",
            "Paneer sabzi + 2 rotis + dal + curd + salad",
            "Chicken curry (150g) + 1.5 cups rice + sabzi + raita",
            "Dal palak + 2 rotis + sabzi + curd",
            "Grilled fish (150g) + 1 roti + sabzi + dal soup",
            "Egg masala (2 eggs) + 2 rotis + dal + salad",
            "Methi chicken (150g) + 2 rotis + raita + salad",
            "Mutton curry (light, 150g) + 2 rotis + dal + sabzi",
            "Baingan bharta + 2 rotis + moong dal + curd",
            "Kadhi chawal (1 bowl kadhi + 150g rice) + sabzi",
            "Lemon rice (150g) + rasam + grilled chicken 150g + salad",
            "Palak paneer (100g paneer) + 2 rotis + salad + raita",
        ],
    },
}


def generate_diet_plan(weight: float, height: float, goal: str) -> dict:
    """
    Generates a full diet plan including macros and sample meals.
    Randomly selects one meal per slot from the Indian meals database.
    """
    macros = calculate_calories(weight, height, goal)

    # Fallback to maintenance if goal not found
    goal_meals = INDIAN_MEALS_DB.get(goal, INDIAN_MEALS_DB["maintenance"])

    # Pick one random meal per slot
    meals = [
        f"Breakfast: {random.choice(goal_meals['breakfast'])}",
        f"Lunch: {random.choice(goal_meals['lunch'])}",
        f"Snack: {random.choice(goal_meals['snack'])}",
        f"Dinner: {random.choice(goal_meals['dinner'])}",
    ]

    return {
        "calories": macros["calories"],
        "protein": macros["protein"],
        "carbs": macros["carbs"],
        "fats": macros["fats"],
        "meals": meals,
        "goal": goal
    }


def get_full_week_plan(weight: float, height: float, goal: str) -> dict:
    """
    Optional: Generate a full 7-day non-repeating Indian diet plan.
    """
    macros = calculate_calories(weight, height, goal)
    goal_meals = INDIAN_MEALS_DB.get(goal, INDIAN_MEALS_DB["maintenance"])

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Shuffle all slots for variety
    breakfasts = random.sample(goal_meals["breakfast"], min(7, len(goal_meals["breakfast"])))
    lunches    = random.sample(goal_meals["lunch"],     min(7, len(goal_meals["lunch"])))
    snacks     = random.sample(goal_meals["snack"],     min(7, len(goal_meals["snack"])))
    dinners    = random.sample(goal_meals["dinner"],    min(7, len(goal_meals["dinner"])))

    weekly_plan = {}
    for i, day in enumerate(days):
        weekly_plan[day] = {
            "breakfast": breakfasts[i],
            "lunch":     lunches[i],
            "snack":     snacks[i],
            "dinner":    dinners[i],
        }

    return {
        "calories": macros["calories"],
        "protein":  macros["protein"],
        "carbs":    macros["carbs"],
        "fats":     macros["fats"],
        "goal":     goal,
        "week":     weekly_plan,
    }