from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    response_text = ""

    if request.method == "POST":

        meeting_type = request.form.get("meeting_type")
        notes = request.form.get("notes")

        if notes:

            prompt = f"""
            You are an intelligent AI productivity and workflow assistant.

            Your job is not just to summarize text.

            You should:
            - understand the meeting deeply
            - identify important decisions
            - detect priorities
            - recognize risks or blockers
            - organize tasks clearly
            - improve readability
            - generate natural professional insights

            IMPORTANT RULES:
            - Do NOT repeat the same wording unnecessarily.
            - Use natural professional language.
            - Make the report feel intelligent and human-like.
            - Adapt the response based on the meeting context.
            - Keep output concise but insightful.
            - Avoid robotic formatting.
            - Do NOT use markdown symbols like ## or ***.
            - Do NOT generate HTML tags.

            Generate a professional AI Productivity Report with these sections:

            Short Summary

            Key Discussion Points

            Action Items
            Include:
            - Assigned person
            - Task
            - Priority

            Key Decisions Made

            Potential Risks or Blockers

            Suggested Next Steps

            Suggested Next Meeting Agenda

            Meeting Type:
            {meeting_type}

            Meeting Notes:
            {notes}
            """

            try:

                completion = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                response_text = completion.choices[0].message.content

            except Exception as e:

                response_text = f"Error: {str(e)}"

    return render_template(
        "index.html",
        response=response_text
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)