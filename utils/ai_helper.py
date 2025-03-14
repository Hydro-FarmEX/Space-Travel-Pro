import os
import json
from openai import OpenAI

openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_travel_tips(user_bookings):
    try:
        booking_history = "\n".join([
            f"- Trip to {booking['destination']} in {booking['class']}" 
            for booking in user_bookings
        ])

        prompt = f"""Based on the following space travel booking history, provide 
        personalized travel tips and recommendations:

        Booking History:
        {booking_history}

        Please provide 3 travel tips in JSON format with 'tips' array."""

        response = openai.chat.completions.create(
            model="gpt-4",  # Using the stable GPT-4 model
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        return response.choices[0].message.content
    except Exception as e:
        return json.dumps({"tips": ["Based on your interest in space travel, consider starting with shorter trips to get acclimated.",
                                  "Pack light and focus on essential items approved for space travel.",
                                  "Take advantage of pre-flight training programs to prepare for your journey."]})