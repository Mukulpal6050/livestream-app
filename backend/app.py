from flask import Flask, jsonify
from flask_cors import CORS
from config import PORT
from routes.overlay_routes import overlay_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(overlay_bp)

@app.route('/')
def home():
    return jsonify({"message": "RTSP Livestream Backend is running 🚀"})

if __name__ == '__main__':
    # listen on all interfaces for dev; change host for production
    app.run(debug=True, port=PORT, host="0.0.0.0")
