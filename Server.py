from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

# Define artifacts and their corresponding images
ARTIFACTS = [
    {"title": "AlphaGo", "image": "static/ArtificalImages/alphago1.jpg", "text_file": "alphago.txt"},
    {"title": "ChatGPT", "image": "static/ArtificalImages/chatgpt1.jpg", "text_file": "chatgpt.txt"},
    {"title": "Ford Assembly Line", "image": "static/industrialImages/fordassembly1.jpg", "text_file": "fordsassemblyline.txt"},
    {"title": "Steam Engine", "image": "/static/industrialImages/steamengine1.jpg", "text_file": "steamengine.txt"},
    {"title": "World Economic Reports", "image": "static/ArtificalImages/worldecon1.jpg", "text_file": "worldecconomic.txt"},
    {"title": "Sadler Committee Report", "image": "static/industrialImages/sadlercommite1.jpg", "text_file": "sadlercommitereport.txt"}
]

def load_artifact_text(file_name):
    """Load text from artifact files."""
    file_path = os.path.join("TextForArtifacts", file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    return "No description available."

@app.route('/')
def home():
    """Serve the homepage."""
    return render_template("homepage.html")

@app.route('/artifacts')
def get_artifacts():
    """Serve artifact data as JSON."""
    artifacts_data = [
        {
            "title": artifact["title"],
            "image": artifact["image"],
            "text": load_artifact_text(artifact["text_file"])
        }
        for artifact in ARTIFACTS
    ]
    return jsonify(artifacts_data)

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files."""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)