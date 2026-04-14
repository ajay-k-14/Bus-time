"""
Bus Time Tracking System - Flask Backend
=========================================
This is the main backend file. It connects to MongoDB and
exposes API endpoints for the frontend to consume.

Run: python app.py
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os

# ── App Setup ──────────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)  # Allow requests from our frontend (different port)

# ── MongoDB Connection ─────────────────────────────────────────────────────────
# Change this URI if your MongoDB runs on a different host / port
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["bus_tracker"]          # Database name
buses_col = db["buses"]             # Collection name


# ── Helper: Calculate Travel Time ─────────────────────────────────────────────
def calc_travel_time(departure: str, arrival: str) -> str:
    """
    Compute travel duration from two HH:MM strings.
    Handles midnight crossover (e.g. 23:30 → 02:00 = 2h 30m).
    Returns a human-readable string like '2h 30m'.
    """
    fmt = "%H:%M"
    dep = datetime.strptime(departure, fmt)
    arr = datetime.strptime(arrival, fmt)

    # If arrival is earlier than departure, it crossed midnight – add 24 h
    diff_minutes = int((arr - dep).total_seconds() / 60)
    if diff_minutes < 0:
        diff_minutes += 24 * 60

    hours, mins = divmod(diff_minutes, 60)
    return f"{hours}h {mins:02d}m"


# ── Endpoint: GET /routes ──────────────────────────────────────────────────────
@app.route("/routes", methods=["GET"])
def get_routes():
    """
    Returns a sorted list of unique locations that appear as
    either the 'from' or 'to' field across all bus documents.
    """
    froms = buses_col.distinct("from")
    tos   = buses_col.distinct("to")
    locations = sorted(set(froms + tos))
    return jsonify({"locations": locations})


# ── Endpoint: GET /buses?from=...&to=... ──────────────────────────────────────
@app.route("/buses", methods=["GET"])
def get_buses():
    """
    Query buses matching the requested origin and destination.
    Travel time is CALCULATED here (not stored in DB).
    """
    from_loc = request.args.get("from", "").strip()
    to_loc   = request.args.get("to", "").strip()

    if not from_loc or not to_loc:
        return jsonify({"error": "Please provide 'from' and 'to' query params."}), 400

    # Case-insensitive search
    query = {
        "from": {"$regex": f"^{from_loc}$", "$options": "i"},
        "to":   {"$regex": f"^{to_loc}$",   "$options": "i"},
    }
    results = list(buses_col.find(query, {"_id": 0, "route_coordinates": 0}))

    # Dynamically compute travel time for every bus
    for bus in results:
        bus["travel_time"] = calc_travel_time(bus["departure_time"], bus["arrival_time"])

    return jsonify({"buses": results})


# ── Endpoint: GET /track/<bus_id> ─────────────────────────────────────────────
@app.route("/track/<bus_id>", methods=["GET"])
def track_bus(bus_id):
    """
    Returns route_coordinates for the given bus_id so the
    frontend can animate the bus marker on a Leaflet map.
    """
    bus = buses_col.find_one({"bus_id": bus_id}, {"_id": 0})
    if not bus:
        return jsonify({"error": f"Bus '{bus_id}' not found."}), 404

    return jsonify({
        "bus_id":   bus["bus_id"],
        "bus_name": bus["bus_name"],
        "from":     bus["from"],
        "to":       bus["to"],
        "coordinates": bus.get("route_coordinates", []),
    })


# ── Dev Server ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)

