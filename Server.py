from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

# Updated artifact list
ARTIFACTS = [
    # Artificial Intelligence Revolution
    {"title": "Alphago", "image": "static/ArtificalImages/alphago1.jpg", "text_file": "alphago.txt"},
    {"title": "Chatgpt", "image": "static/ArtificalImages/chatgpt1.jpg", "text_file": "chatgpt.txt"},
    {"title": "Worldeccon forum", "image": "static/ArtificalImages/worldecon1.jpg", "text_file": "worldecconomic.txt"},
    {"title": "Ai in stock trading", "image": "static/ArtificalImages/aiStockT1.jpg", "text_file": "ai_stock_trading.txt"},
    {"title": "Dalle", "image": "static/ArtificalImages/dalle1.jpg", "text_file": "dalle.txt"},
    {"title": "Ai in warefare drones", "image": "static/ArtificalImages/aiWareFare1.jpg", "text_file": "ai_warfare_drones.txt"},
    # Industrial Revolution
    {"title": "Assembly line", "image": "static/industrialImages/fordassembly1.jpg", "text_file": "fordsassemblyline.txt"},
    {"title": "Steam engine", "image": "static/industrialImages/steamengine1.jpg", "text_file": "steamengine.txt"},
    {"title": "Sadler committee report", "image": "static/industrialImages/sadlercommite1.jpg", "text_file": "sadlercommitereport.txt"},
    {"title": "Iww", "image": "static/industrialImages/IWW1.jpg", "text_file": "iww.txt"},
    {"title": "Spinning jenny", "image": "static/industrialImages/spinningjenny1.jpg", "text_file": "spinning_jenny.txt"},
    {"title": "Combustion engine", "image": "static/industrialImages/combustion1.jpg", "text_file": "combustion_engine.txt"}
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
            "text": load_artifact_text(artifact["text_file"]).replace("\n", "<br>")
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