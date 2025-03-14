import json
import os
import logging
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_chat_response(user_message):
    try:
        logger.debug(f"Generating chat response for message: {user_message}")

        system_prompt = """You are a helpful space travel assistant for our luxury space tourism company. 
        You help customers with:
        - Information about destinations (Mars Colony: $1.5M, Lunar Base: $750K, Space Station: $500K)
        - Booking procedures and requirements
        - Trip preparation and safety measures
        - Accommodation options and amenities
        - Payment plans and cancellation policies

        Keep responses concise (max 2-3 sentences), friendly, and focused on space travel topics.
        If you don't know something, admit it and suggest contacting our customer service.
        """

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        response = openai.completions.create(
            model="text-davinci-003",  # Using older model which might be available by default
            prompt=f"{system_prompt}\n\nUser: {user_message}\nAssistant:",
            max_tokens=150,
            temperature=0.7,
            stop=["User:", "Assistant:"]
        )

        logger.debug("Successfully generated OpenAI response")
        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Error generating chat response: {str(e)}")
        return "I'm currently experiencing connectivity issues. For immediate assistance, please try our contact form or email support@spacetravel.com."