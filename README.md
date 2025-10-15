# 🎥 RTSP Livestream Player with Overlay Manager

A full-stack web application that allows users to **watch RTSP livestreams** directly in the browser, with the ability to **add, position, and save text or logo overlays** dynamically.

---

![App Screenshot](frontend/public/home.png)

## 🚀 Features

### 🎬 Livestream Player
- Enter any RTSP URL and play a live video stream.
- Supports **play, pause, and volume control**.
- Real-time video playback powered by a compatible RTSP-to-WebRTC player.

### 🖋️ Overlay Manager
- Add **text overlays** or **logo overlays** dynamically.
- Drag and resize overlays anywhere on the video.
- Manage overlays easily with CRUD operations.

### ⚙️ Overlay CRUD API
- **Create** custom overlays (text/logo, size, position).
- **Read** saved overlays and auto-load them on page refresh.
- **Update** overlays after repositioning or resizing.
- **Delete** overlays with one click.

---

## 🧱 Tech Stack

| Layer | Technology Used |
|--------|----------------|
| **Frontend** | React.js, Tailwind CSS, react-rnd |
| **Backend** | Python Flask |
| **Database** | MongoDB (Atlas) |
| **Streaming** | RTSP / WebRTC compatible player |

---

## 📁 Folder Structure

project-root/
│
├── backend/
│ ├── app.py # Flask entry point
│ ├── config.py # MongoDB and app configuration
│ ├── routes/
│ │ └── overlay_routes.py # Overlay CRUD routes
│ └── requirements.txt # Dependencies
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── VideoPlayer.jsx
│ │ │ ├── OverlayManager.jsx
│ │ │ └── OverlayItem.jsx
│ │ ├── App.jsx
│ │ └── index.js
│ ├── package.json
│ └── tailwind.config.js
│
└── README.md




---

## ⚙️ Backend Setup (Flask + MongoDB)

### 1️⃣ Navigate to backend folder



cd backend



## create virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt


.env

MONGO_URI = your_mongodb_connection_string


### run backend:  python app.py

Backend will run on: http://localhost:5000

Frontend Setup (React)

cd frontend
npm install
npm start

Frontend will run on: http://localhost:3000


🔗 API Endpoints
Method	Endpoint	Description
GET	/api/overlays	Get all saved overlays
POST	/api/overlays	Create a new overlay
PUT	/api/overlays/:id	Update overlay (position, size, or content)
DELETE	/api/overlays/:id	Delete overlay
🧠 How to Use

Open the frontend → Enter an RTSP URL (e.g., rtsp://rtsp.me/demo1234).

Click Play Stream to start video playback.

Use Add Text Overlay or Add Logo Overlay to place overlays.

Drag, resize, and position overlays freely.

Click Save Overlay to store the layout in MongoDB.

Reload the page — saved overlays will automatically appear.

📸 Demo Preview

🧾 Documentation
API Docs

All CRUD API endpoints are documented inside /backend/routes/overlay_routes.py with comments.

User Guide

Open app → Paste RTSP URL → Play → Add Overlays

Manage overlays (edit/delete) from the Saved Overlays section

🌍 Deployment Guide
Backend (Render)

Create new Web Service on Render.com

Connect GitHub repo and set build command:

pip install -r requirements.txt


Add environment variable:

MONGO_URI = your_mongodb_connection_string


Deploy → Copy the Render backend URL.

Frontend (Vercel)

Push frontend to GitHub.

Import project into Vercel.com
.

Set VITE_BACKEND_URL as the Render backend URL.

Deploy and test live!

🧑‍💻 Author

Mukul Pal
📧 mukulpal6050@gmail.com

💻 GitHub: Mukulpal6050

🌐 Portfolio

⭐ Future Improvements

Add live chat with stream.

WebRTC-based direct RTSP to browser conversion.

Overlay templates and animation support.
