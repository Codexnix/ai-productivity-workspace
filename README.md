 AI Meeting Notes Summarizer

Transform raw, messy meeting notes into clean, structured summaries and actionable insights — powered by Google Gemini AI.


✨ Features
FeatureDetailsShort Summary2–3 sentence TL;DR of the entire meetingKey Discussion PointsBullet-point list of topics coveredAction ItemsTasks with owners (when mentioned)High Priority TasksUrgent/critical items flagged separately9 Meeting TypesStandup, Sprint, Retro, Client Call, Board, and moreDownloadExport summary as .txt with one clickDark UIProfessional dark-themed Streamlit interface

📁 Folder Structure
ai-meeting-summarizer/
│
├── app.py               ← Main Streamlit application
├── requirements.txt     ← Python dependencies
├── .env                 ← Your API key (create this, never commit!)
├── .env.example         ← Template for .env
├── .gitignore           ← Excludes secrets & junk from Git
└── README.md            ← This file

🔑 How to Get Your Gemini API Key

Visit Google AI Studio
Sign in with your Google account
Click "Create API Key"
Copy the key — it looks like AIzaSy...
Paste it in your .env file (see setup below)


Free tier gives you 15 requests/minute and 1 million tokens/day — more than enough for personal use.


⚙️ Installation & Setup
Prerequisites

Python 3.9+ installed
pip available in your terminal

Step 1 — Clone or Download the Project
bash# Clone
git clone https://github.com/yourusername/ai-meeting-summarizer.git
cd ai-meeting-summarizer

# OR simply download and unzip, then open that folder in your terminal
Step 2 — Create a Virtual Environment (Recommended)
bash# Create
python -m venv venv

# Activate — macOS / Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
Step 3 — Install Dependencies
bashpip install -r requirements.txt
Step 4 — Set Up Your API Key
bash# Copy the example file
cp .env.example .env
Now open .env in any text editor and replace the placeholder:
envGEMINI_API_KEY=AIzaSyYOUR_REAL_KEY_HERE
Step 5 — Run the App
bashstreamlit run app.py
The app will open automatically at http://localhost:8501 🎉

🚀 How to Use

Open the app in your browser
Paste your raw meeting notes into the text area
Select the meeting type from the sidebar dropdown
Click ✨ Summarize Notes
View your structured summary in four cards
Click ⬇️ Download Summary as .txt to save


🛠️ Tech Stack
LayerTechnologyFrontendStreamlitAI / LLMGoogle Gemini 1.5 Flash via google-generativeaiConfigpython-dotenvLanguagePython 3.9+

🔒 Security Notes

Never commit your .env file — it is listed in .gitignore
Use .env.example as a safe template to share
For production deployment (e.g. Streamlit Cloud), add your key as a Secret in the dashboard settings instead of a .env file


📦 Dependencies
streamlit>=1.35.0
google-generativeai>=0.7.0
python-dotenv>=1.0.0

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

📄 License
MIT License — free to use, modify, and distribute.

Built for developers, founders, and teams who take a lot of meetings.