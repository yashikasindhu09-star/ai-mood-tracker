from flask import Flask, render_template, request
from ai_analysis import analyze_mood

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mood = suggestion = None
    if request.method == "POST":
        text = request.form["journal"]
        mood, suggestion = analyze_mood(text)
    return render_template("index.html", mood=mood, suggestion=suggestion)

app.run(debug=True)
