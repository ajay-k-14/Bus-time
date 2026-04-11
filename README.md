# 🚌 BusTrack Kerala — Bus Time Tracking System

A full-stack bus tracking web application built with:
- **Frontend**: HTML + CSS + Vanilla JavaScript
- **Backend**: Python / Flask
- **Database**: MongoDB

---

## 📁 Project Structure

```
bus-tracker/
├── backend/
│   ├── app.py            ← Flask API server
│   ├── seed_data.py      ← Populate MongoDB with sample data
│   └── requirements.txt  ← Python dependencies
└── frontend/
    ├── index.html        ← Main page
    ├── style.css         ← Styles
    └── script.js         ← App logic
```

---

## ⚙️ Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.9+ |
| MongoDB | 6.0+ (Community Edition) |
| pip | latest |

---

## 🔧 1 — MongoDB Setup

### Install MongoDB (if not already installed)
- **Ubuntu/Debian**: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
- **macOS** (Homebrew): `brew tap mongodb/brew && brew install mongodb-community`
- **Windows**: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

### Start MongoDB
```bash
# Linux / macOS
sudo systemctl start mongod      # OR
mongod --dbpath /data/db

# Windows (run in PowerShell as admin)
net start MongoDB
```

### Verify MongoDB is running
```bash
mongosh
# You should see a ">" prompt — type "exit" to quit
```

---

## 🐍 2 — Backend Setup

```bash
# Navigate to backend folder
cd bus-tracker/backend

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Seed the database with sample bus data (run ONCE)
python seed_data.py
# Expected output: ✅ Inserted 7 buses into MongoDB.

# Start the Flask server
python app.py
# Expected output: Running on http://127.0.0.1:5000
```

---

## 🌐 3 — Frontend Setup

No build step needed. Simply open the HTML file:

```bash
# From the project root, just open in a browser:
open bus-tracker/frontend/index.html      # macOS
xdg-open bus-tracker/frontend/index.html  # Linux
# Windows: double-click index.html in Explorer

# OR serve with Python (avoids any CORS quirks)
cd bus-tracker/frontend
python -m http.server 8080
# Then visit: http://localhost:8080
```

---

## 🚀 Running the Full App

1. Start MongoDB
2. `cd backend && python app.py`  (Flask on port 5000)
3. Open `frontend/index.html` in your browser
4. Select **From** and **To** locations, click **Search Buses**
5. Click **Track Bus** to see live route animation on the map

---

## 🔌 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/routes` | All unique locations |
| GET | `/buses?from=X&to=Y` | Buses on a route (travel time calculated) |
| GET | `/track/<bus_id>` | Route coordinates for a specific bus |

### Example responses

**GET /routes**
```json
{ "locations": ["Ernakulam", "Kozhikode", "Thiruvananthapuram", "Thrissur"] }
```

**GET /buses?from=Kozhikode&to=Thrissur**
```json
{
  "buses": [
    {
      "bus_id": "KL-01",
      "bus_name": "Kerala KSRTC Express",
      "from": "Kozhikode",
      "to": "Thrissur",
      "departure_time": "06:00",
      "arrival_time": "09:30",
      "travel_time": "3h 30m"
    }
  ]
}
```

---

## 📦 MongoDB Document Schema

```json
{
  "bus_id": "KL-01",
  "bus_name": "Kerala KSRTC Express",
  "from": "Kozhikode",
  "to": "Thrissur",
  "departure_time": "06:00",
  "arrival_time": "09:30",
  "route_coordinates": [
    [11.2588, 75.7804],
    [10.9982, 76.0458],
    [10.7867, 76.6548]
  ]
}
```

> ⚠️ `travel_time` is **NOT stored** in the database. It is computed dynamically.

---

## ✅ Sample Routes Available

| Bus ID | Route | Departure | Arrival | Duration |
|--------|-------|-----------|---------|----------|
| KL-01 | Kozhikode → Thrissur | 06:00 | 09:30 | 3h 30m |
| KL-02 | Kozhikode → Thrissur | 08:45 | 12:15 | 3h 30m |
| KL-03 | Thrissur → Ernakulam | 07:30 | 09:00 | 1h 30m |
| KL-04 | Thrissur → Ernakulam | 22:00 | 00:30 | 2h 30m *(midnight crossover)* |
| KL-05 | Ernakulam → Thiruvananthapuram | 05:00 | 09:45 | 4h 45m |
| KL-06 | Kozhikode → Ernakulam | 10:00 | 14:30 | 4h 30m |
| KL-07 | Thiruvananthapuram → Kozhikode | 21:00 | 06:30 | 9h 30m *(overnight)* |

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---------|-----|
| `Connection refused` on port 5000 | Make sure `python app.py` is running |
| `ServerSelectionTimeoutError` | MongoDB is not running — start `mongod` |
| Empty dropdown lists | Check Flask is running and seed data was loaded |
| Map not showing | Allow browser to load external scripts (Leaflet CDN) |
| CORS error in browser console | Ensure `flask-cors` is installed; `pip install flask-cors` |
