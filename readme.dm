🚀 Space Travel Booking Platform this project was implemented using GPT4 and Replit prompts as a part of the global prompt engineering championship Dubai 2025
The Future of Space Tourism 🌍✨
Welcome to Space Travel Booking Platform, the ultimate gateway to commercial space travel! This initiative is inspired by the UAE leadership and Dubai Future Foundation, transforming Dubai into the world’s first hub for space tourism. 🚀

🌟 Features
✅ Trip Scheduling & Booking – Reserve your seat for space station visits, Moon landings, and Mars missions.
✅ Pricing & Packages – Choose between Luxury Cabins, Economy Shuttles, and VIP Zero-Gravity Experiences.
✅ Accommodation Recommendations – Book lunar hotels, space stations, and orbital stays.
✅ User Dashboard – Manage trips, countdown to launch, and AI-powered space travel tips.
✅ Multilingual Support (English & Arabic) – Users can switch languages dynamically.
✅ NFT-Based Ticketing – Space tickets are minted as NFTs, serving as proof of travel.
✅ Leaderboard & Achievements – Gamified experience rewarding frequent travelers.
✅ Interactive Map (Launch Pad at Museum of the Future, Dubai) – Displays the departure site & trip paths.

📂 Project Structure
📦 Hydro-FarmEX
│── 📂 attached_assets        # Stores assets like images, icons, and other UI elements
│── 📂 static                 # CSS, JavaScript, and frontend static assets
│── 📂 templates              # HTML templates for the web application
│── 📂 utils                  # Helper functions and utilities
│── 📄 .replit                # Replit configuration file
│── 📄 generated-icon.png      # Project icon
│── 📄 main.py                # Flask backend for API routes
│── 📄 pyproject.toml         # Python project dependencies
│── 📄 replit.nix             # Replit environment configuration
│── 📄 uv.lock                # Dependency lock file
🚀 Deployment Guide
You can deploy this project on Render (Backend) & Vercel (Frontend).

1️⃣ Deploy the Backend (Flask) on Render
Push the Code to GitHub
Ensure your latest code is committed:

git add .
git commit -m "Deploy Flask backend"
git push origin main
Create a New Render Web Service
Go to Render and sign up/log in.
Click New Web Service → Connect to your GitHub Repo.
Select main.py as the entry point.
Set Start Command to:
gunicorn -w 4 -b 0.0.0.0:5000 main:app
Click Deploy and get your backend API URL.
2️⃣ Deploy the Frontend (React) on Vercel
Push the Frontend Code to GitHub:
git add .
git commit -m "Deploy React frontend"
git push origin main
Deploy on Vercel
Sign up/log in to Vercel.
Click New Project → Select your GitHub Repo.
Choose the default React settings and Deploy.
Your site is now live! 🎉
📡 Environment Variables
Before deployment, configure .env variables on Render/Vercel:

Variable	Description
FLASK_SECRET_KEY	Flask security key
DATABASE_URL	Database connection URL
NFT_API_KEY	API Key for NFT Minting
OPENAI_API_KEY	API Key for AI assistant
GOOGLE_MAPS_API_KEY	API Key for interactive maps
🎯 How to Run Locally
Clone the Repo

git clone https://github.com/yourusername/Hydro-FarmEX.git
cd Hydro-FarmEX
Set Up Python Virtual Environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install Dependencies

pip install -r requirements.txt
Run the Backend

python main.py
Run the Frontend

cd static
npm install
npm start
Access the App
Open http://localhost:3000/ for the frontend.
Open http://localhost:5000/ for the backend.
🔥 Contributors
💡 Your Name – Lead Developer
💡 Team Members – Contributors

⭐ Future Enhancements
🔹 AI Voice Assistant for space guidance
🔹 3D Virtual Reality Previews of space hotels
🔹 Live Space Trip Streaming for travelers

🎉 Enjoy your journey beyond Earth! 🚀🌍

