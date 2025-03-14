import os
import logging
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from utils.ai_helper import get_travel_tips
from utils.mock_data import trips, accommodations, users, bookings
from utils.chat_helper import generate_chat_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book')
def book():
    return render_template('booking.html', trips=trips)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/dashboard')
def dashboard():
    # In a real app, we would get the user ID from session
    user_bookings = bookings.get("user123", [])
    return render_template('dashboard.html', bookings=user_bookings)

@app.route('/accommodations')
def accommodations_page():
    return render_template('accommodations.html', accommodations=accommodations)

# API Endpoints
@app.route('/api/book_trip', methods=['POST'])
def book_trip():
    try:
        data = request.json
        trip_id = data.get('trip_id')
        user_id = "user123"  # In production, get from session
        wallet_address = data.get('wallet_address')
        
        if trip_id not in trips:
            return jsonify({"error": "Invalid trip ID"}), 400
            
        if user_id not in bookings:
            bookings[user_id] = []
        
        trip_data = trips[trip_id].copy()
        bookings[user_id].append(trip_data)
        
        # Mint NFT ticket
        if wallet_address:
            receipt = mint_space_ticket(wallet_address, trip_data)
            if receipt:
                trip_data['nft_token_id'] = receipt['tokenId']
        
        # Check for achievements
        new_achievements = achievement_system.check_achievements(user_id, trip_data)
        
        return jsonify({
            "message": "Booking successful",
            "nft_minted": bool(receipt if wallet_address else False),
            "new_achievements": new_achievements
        })
    except Exception as e:
        logger.error(f"Booking error: {str(e)}")
        return jsonify({"error": "Booking failed"}), 500

@app.route('/api/ai_tips', methods=['GET'])
def ai_tips():
    try:
        user_id = "user123"  # In production, get from session
        user_bookings = bookings.get(user_id, [])
        tips = get_travel_tips(user_bookings)
        return jsonify({"tips": tips})
    except Exception as e:
        logger.error(f"AI tips error: {str(e)}")
        return jsonify({"error": "Failed to get travel tips"}), 500



@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify(achievement_system.get_leaderboard())

@app.route('/api/user/achievements', methods=['GET'])
def get_user_achievements():
    user_id = "user123"  # In production, get from session
    return jsonify({
        "achievements": achievement_system.user_achievements[user_id],
        "points": achievement_system.user_points[user_id]
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message')
        if not message:
            logger.warning("Chat request received with no message")
            return jsonify({"error": "No message provided"}), 400

        # Special handling for UAE question
        if "where are you from" in message.lower():
            return jsonify({
                "response": "I was trained in the digital cosmos, but my heart belongs to the UAE and the Museum of the Future! 🚀"
            })

        logger.info(f"Processing chat message: {message[:50]}...")
        response = generate_chat_response(message)

        if not response:
            logger.error("Empty response received from chat generator")
            return jsonify({"error": "Failed to generate response"}), 500

        logger.info("Successfully generated chat response")
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({
            "error": "Failed to process chat message",
            "message": "Our AI assistant is temporarily unavailable. Please try again shortly."
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)