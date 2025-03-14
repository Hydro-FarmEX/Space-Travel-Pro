import os
import logging
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from utils.ai_helper import get_travel_tips
from utils.mock_data import trips, accommodations, users, bookings

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
        
        if trip_id not in trips:
            return jsonify({"error": "Invalid trip ID"}), 400
            
        if user_id not in bookings:
            bookings[user_id] = []
            
        bookings[user_id].append(trips[trip_id])
        return jsonify({"message": "Booking successful"})
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
