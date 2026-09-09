import os
import time
from google import genai
from google.genai import types

# Keyword fallback responses — used when AI quota is exhausted
FALLBACK_REPLIES = {
    "workout": "💪 **Workout Tip:** Focus on compound movements — squats, deadlifts, bench press, and rows. These hit the most muscle groups and give you the biggest strength gains per hour in the gym.",
    "diet": "🥗 **Diet Tip:** Build every meal around a lean protein source (chicken, fish, eggs or tofu). Protein keeps you full, builds muscle, and has the highest thermic effect.",
    "calorie": "🔥 For muscle gain: TDEE + 300 kcal/day. For fat loss: TDEE - 500 kcal/day. Calculate your TDEE at tdee.com and track for 2 weeks.",
    "protein": "🥩 Aim for **1.6–2.2g of protein per kg of bodyweight** daily. Best sources: chicken breast, Greek yogurt, eggs, whey protein, lentils, and fish.",
    "sleep": "😴 **Sleep is your secret weapon.** You grow muscle during sleep, not during the workout. Aim for 7–9 hours with a consistent schedule.",
    "habit": "📈 **Consistency beats intensity.** Start with 3 days/week and build up. Log your workouts — what gets measured gets improved.",
    "cardio": "🏃 HIIT 2–3x per week is best for fat loss without sacrificing muscle. Keep steady-state sessions under 45 minutes.",
    "stress": "🧘 High cortisol from stress can stall fat loss and muscle gain. Try 10 minutes of deep breathing or a short walk.",
    "fat": "🔥 For fat loss: maintain a 300–500 kcal deficit, prioritize protein, lift weights to preserve muscle, and add cardio 2–3x/week.",
    "muscle": "💪 To build muscle: eat in a 200–300 kcal surplus, hit 1.6–2.2g protein/kg, sleep 8 hours, and progressively overload your lifts.",
}

def get_fallback(message: str) -> str:
    lower = message.lower()
    for keyword, reply in FALLBACK_REPLIES.items():
        if keyword in lower:
            return reply + "\n\n*⚡ AI quota refreshes soon — try again shortly for full AI responses!*"
    return "🤖 I'm your FIT-AI coach! Ask me about workouts, diet, protein, sleep, or habits. *(AI quota temporarily at limit — smart responses still available!)*"


class GeminiBot:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.is_configured = bool(self.api_key)
        self.history = []

        self.system_instruction = (
            "You are FIT-AI, an elite and highly knowledgeable AI Fitness Coach. "
            "Your goal is to help users with workouts, diet, nutrition, sleep, habits, and wellness. "
            "Rules: "
            "1. Keep responses concise, actionable, and encouraging. "
            "2. Use bullet points or bold text for clarity where appropriate. "
            "3. If asked something completely unrelated to health or fitness, politely redirect to fitness topics. "
            "4. Do not provide medical diagnoses. Advise consulting a doctor for injuries or serious conditions. "
            "5. Speak like a world-class personal trainer — confident and motivating."
        )

        # Models to try in order (lite model has higher free tier quota)
        self.models = [
            "models/gemini-2.0-flash-lite",
            "models/gemini-2.0-flash",
            "models/gemini-2.5-flash",
        ]

        if self.is_configured:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    def ask(self, message: str) -> str:
        if not self.is_configured or self.client is None:
            return "Please configure the GEMINI_API_KEY in your .env file to activate AI responses. 🚀"

        self.history.append(types.Content(
            role="user",
            parts=[types.Part(text=message)]
        ))

        for model_name in self.models:
            for attempt in range(2):
                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=self.history,
                        config=types.GenerateContentConfig(
                            system_instruction=self.system_instruction,
                            temperature=0.7,
                            max_output_tokens=512,
                        )
                    )
                    reply = response.text
                    self.history.append(types.Content(
                        role="model",
                        parts=[types.Part(text=reply)]
                    ))
                    return reply

                except Exception as e:
                    err = str(e)
                    if "429" in err or "RESOURCE_EXHAUSTED" in err:
                        if attempt == 0:
                            time.sleep(2)
                            continue
                        break  # try next model
                    return f"AI Error: {err}"

        # All models rate-limited — gracefully fall back to keyword responses
        self.history.pop()
        return get_fallback(message)


# Global singleton instance
gemini_bot = GeminiBot()
