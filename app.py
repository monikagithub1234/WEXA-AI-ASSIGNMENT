from flask import Flask, render_template_string, request, send_from_directory
from graph_queries import get_career_details

app = Flask(__name__)

@app.route("/style.css")
def serve_css():
    return send_from_directory(".", "style.css")

def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/", methods=["GET", "POST"])
def index():

    details = None

    if request.method == "POST":
        user_input = request.form["career_input"]
        details = get_career_details(user_input)

    html = load_html()
    return render_template_string(html, details=details)

if __name__ == "__main__":
    app.run(debug=True)