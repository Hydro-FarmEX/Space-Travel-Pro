
from collections import defaultdict

ACHIEVEMENTS = {
    "FIRST_TRIP": {
        "id": "first_trip",
        "name": "Space Pioneer",
        "description": "Completed first space journey",
        "icon": "🚀"
    },
    "MARS_EXPLORER": {
        "id": "mars_explorer",
        "name": "First Martian Tourist",
        "description": "Visited Mars Colony",
        "icon": "🔴"
    },
    "ELITE_EXPLORER": {
        "id": "elite_explorer",
        "name": "Elite Space Explorer",
        "description": "Completed 5+ space trips",
        "icon": "👨‍🚀"
    }
}

class AchievementSystem:
    def __init__(self):
        self.user_achievements = defaultdict(list)
        self.user_points = defaultdict(int)
    
    def check_achievements(self, user_id, booking):
        points = self._calculate_points(booking)
        self.user_points[user_id] += points
        
        # Check for new achievements
        new_achievements = []
        
        # First trip achievement
        if len(self.user_achievements[user_id]) == 0:
            new_achievements.append(ACHIEVEMENTS["FIRST_TRIP"])
            
        # Mars Explorer achievement
        if booking["destination"] == "Mars Colony Alpha":
            if ACHIEVEMENTS["MARS_EXPLORER"] not in self.user_achievements[user_id]:
                new_achievements.append(ACHIEVEMENTS["MARS_EXPLORER"])
        
        # Elite Explorer achievement
        if self.user_points[user_id] >= 5000:
            if ACHIEVEMENTS["ELITE_EXPLORER"] not in self.user_achievements[user_id]:
                new_achievements.append(ACHIEVEMENTS["ELITE_EXPLORER"])
        
        self.user_achievements[user_id].extend(new_achievements)
        return new_achievements
    
    def _calculate_points(self, booking):
        points = 1000  # Base points
        if "vip" in booking.get("class", "").lower():
            points *= 2
        return points
    
    def get_leaderboard(self, limit=10):
        sorted_users = sorted(
            self.user_points.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]
        return [
            {
                "user_id": user_id,
                "points": points,
                "achievements": self.user_achievements[user_id]
            }
            for user_id, points in sorted_users
        ]

achievement_system = AchievementSystem()
