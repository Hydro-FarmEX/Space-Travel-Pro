import os
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
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
        
        Please provide tips in JSON format with 'tips' array."""
        
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Failed to generate travel tips: {str(e)}")
