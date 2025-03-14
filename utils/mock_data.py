
# Mock data for the space travel booking platform
trips = {
    "mars-colony": {
        "id": "mars-colony",
        "destination": "Mars Colony Alpha",
        "departure_date": "2025-12-01",
        "departure_time": "08:00 UTC",
        "spacecraft": "SpaceX Starship MK4",
        "duration": "8 months",
        "price": {
            "economy": 1500000,
            "business": 2500000,
            "vip": 5000000
        },
        "amenities": ["Zero-G Lounge", "Hibernation Pods", "Virtual Earth View", "Space Garden"],
        "crew": {
            "captain": "Sarah Chen",
            "medical_officer": "Dr. James Wilson",
            "engineer": "Elena Rodriguez"
        },
        "experiences": ["Mars Surface EVA", "Olympus Mons Expedition", "Valles Marineris Virtual Tour"],
        "coordinates": {"lat": 25.2048, "lng": 55.2708},
        "available_seats": {"economy": 10, "business": 5, "vip": 2}
    },
    "lunar-base": {
        "id": "lunar-base",
        "destination": "Lunar Base Artemis",
        "departure_date": "2025-10-15",
        "departure_time": "12:00 UTC",
        "spacecraft": "Blue Origin New Armstrong",
        "duration": "5 days",
        "price": {
            "economy": 750000,
            "business": 1200000,
            "vip": 2000000
        },
        "amenities": ["Observation Deck", "Lunar Theater", "Gravity Gym"],
        "crew": {
            "captain": "Michael Chang",
            "pilot": "Lisa Martinez",
            "science_officer": "Dr. Alex Kumar"
        },
        "experiences": ["Lunar Rover Expedition", "Earth Rise Viewing", "Apollo Landing Sites Tour"],
        "coordinates": {"lat": 25.2048, "lng": 55.2708},
        "available_seats": {"economy": 15, "business": 8, "vip": 3}
    },
    "orbital-hotel": {
        "id": "orbital-hotel",
        "destination": "Orbital Grand Hotel",
        "departure_date": "2025-09-01",
        "departure_time": "15:00 UTC",
        "spacecraft": "Virgin Galactic Unity",
        "duration": "14 days",
        "price": {
            "economy": 500000,
            "business": 800000,
            "vip": 1500000
        },
        "amenities": ["Zero-G Restaurant", "Space Spa", "Infinity Pool", "Star Observation Deck"],
        "crew": {
            "hotel_manager": "David Park",
            "chef": "Marie Dubois",
            "activities_director": "Juan Carlos"
        },
        "experiences": ["Spacewalk Experience", "Zero-G Dancing", "Orbital Sunrise Meditation"],
        "coordinates": {"lat": 25.2048, "lng": 55.2708},
        "available_seats": {"economy": 20, "business": 10, "vip": 5}
    }
}

accommodations = {
    "mars-hilton": {
        "id": "mars-hilton",
        "name": "Mars Hilton",
        "type": "Luxury Dome",
        "price_per_night": 50000,
        "description": "5-star luxury dome with Earth view",
        "amenities": ["Artificial Gravity", "Private Garden", "VR Earth Connection"]
    },
    "lunar-lodge": {
        "id": "lunar-lodge",
        "name": "Lunar Lodge",
        "type": "Standard Pod",
        "price_per_night": 25000,
        "description": "Comfortable pods with basic amenities",
        "amenities": ["Moon View", "Exercise Area", "Common Lounge"]
    },
    "orbital-suite": {
        "id": "orbital-suite",
        "name": "Orbital Suite",
        "type": "Space Hotel",
        "price_per_night": 35000,
        "description": "Luxury orbital accommodation with Earth views",
        "amenities": ["Zero-G Sleeping", "Observation Deck", "Space Restaurant"]
    }
}

users = {
    "user123": {
        "id": "user123",
        "name": "Sarah Armstrong",
        "email": "sarah@example.com",
        "avatar": "👩‍🚀",
        "preferences": ["Luxury", "Long Duration"],
        "points": 12500,
        "achievements": ["🚀 First Trip", "🌟 Elite Explorer", "🔴 Mars Pioneer"]
    },
    "user456": {
        "id": "user456",
        "name": "Alex Chen",
        "email": "alex@example.com",
        "avatar": "👨‍🚀",
        "preferences": ["Adventure", "Science"],
        "points": 9800,
        "achievements": ["🚀 First Trip", "🌙 Lunar Explorer"]
    },
    "user789": {
        "id": "user789",
        "name": "Elena Kumar",
        "email": "elena@example.com",
        "avatar": "👩‍🚀",
        "preferences": ["VIP", "Photography"],
        "points": 15200,
        "achievements": ["🚀 First Trip", "🌟 Elite Explorer", "🌍 Earth Orbit Master"]
    },
    "user101": {
        "id": "user101",
        "name": "Marcus Williams",
        "email": "marcus@example.com",
        "avatar": "👨‍🚀",
        "preferences": ["Research", "Extended Stay"],
        "points": 7500,
        "achievements": ["🚀 First Trip", "🔬 Space Scientist"]
    },
    "user102": {
        "id": "user102",
        "name": "Yuki Tanaka",
        "email": "yuki@example.com",
        "avatar": "👩‍🚀",
        "preferences": ["Zero Gravity", "Photography"],
        "points": 11300,
        "achievements": ["🚀 First Trip", "📸 Space Photographer"]
    }
}

bookings = {
    "user123": [],
    "user456": [],
    "user789": [],
    "user101": [],
    "user102": []
}
