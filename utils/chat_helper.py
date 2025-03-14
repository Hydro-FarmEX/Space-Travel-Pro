import json
from openai import OpenAI
import os

openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_chat_response(user_message):
    try:
        system_prompt = """You are a helpful space travel assistant for our luxury space tourism company. 
        You can help with:
        - Information about our destinations (Mars Colony, Lunar Base, Space Station)
        - Booking procedures and requirements
        - Safety measures and preparation
        - Accommodation options
        - Pricing information
        Keep responses concise, friendly, and focused on space travel topics.
        """

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150  # Keep responses concise
        )

        return response.choices[0].message.content
    except Exception as e:
        return "I apologize, but I'm having trouble processing your request at the moment. Please try again later."
