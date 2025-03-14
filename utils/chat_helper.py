import json
import os
import logging
import httpx
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize API clients
openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
GITHUB_COPILOT_API_KEY = os.environ.get("GITHUB_COPILOT_API_KEY")

def generate_copilot_response(user_message):
    """Generate response using GitHub Copilot API"""
    try:
        headers = {
            "Authorization": f"Bearer {GITHUB_COPILOT_API_KEY}",
            "Content-Type": "application/json",
            "OpenAI-Organization": "github-copilot"
        }

        context = """You are a helpful space travel assistant for a luxury space tourism company.
        You help customers with:
        - Information about destinations (Mars Colony: $1.5M, Lunar Base: $750K, Space Station: $500K)
        - Booking procedures and requirements
        - Trip preparation and safety measures
        - Accommodation options and amenities
        - Payment plans and cancellation policies

        Keep responses concise, friendly, and focused on space travel topics."""

        data = {
            "prompt": f"{context}\n\nUser: {user_message}\nAssistant:",
            "max_tokens": 150,
            "temperature": 0.7,
            "stop": ["User:", "Assistant:"]
        }

        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                "https://api.githubcopilot.com/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["text"].strip()
            else:
                logger.error(f"Copilot API error: {response.status_code} - {response.text}")
                return None
    except Exception as e:
        logger.error(f"Error generating Copilot response: {str(e)}")
        return None

def generate_chat_response(user_message):
    """Generate chat response using OpenAI with Copilot fallback"""
    try:
        logger.debug(f"Attempting OpenAI response for message: {user_message}")

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

        response = openai.completions.create(
            model="text-davinci-003",
            prompt=f"{system_prompt}\n\nUser: {user_message}\nAssistant:",
            max_tokens=150,
            temperature=0.7,
            stop=["User:", "Assistant:"]
        )

        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"OpenAI error: {str(e)}")
        logger.info("Attempting fallback to Copilot")

        copilot_response = generate_copilot_response(user_message)
        if copilot_response:
            return copilot_response

        return "I'm currently experiencing connectivity issues. For immediate assistance, please try our contact form or email support@spacetravel.com."