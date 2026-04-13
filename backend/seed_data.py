"""
seed_data.py – Run this ONCE to populate MongoDB with sample buses.
Usage: python seed_data.py
"""

from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["bus_tracker"]
buses_col = db["buses"]

# Clear existing data (safe for dev)
buses_col.drop()

sample_buses = [

    # ── Route 1: Bandadka → Kasaragod ───────────────────────────────────────    
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "05:30",
        "arrival_time": "07:20",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "06:30",
        "arrival_time": "08:20",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "07:10",
        "arrival_time": "09:00",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "07:45",
        "arrival_time": "09:35",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "08:45",
        "arrival_time": "10:35",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "10:40",
        "arrival_time": "12:30",
        "route_coordinates": [
            [11.2588, 75.7804],
            [11.1085, 75.9874],
            [10.9982, 76.0458],
            [10.8350, 76.2710],
            [10.7867, 76.6548],
        ],
    },
    
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "11:00",
        "arrival_time": "12:50",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "11:20",
        "arrival_time": "13:10",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "16:30",
        "arrival_time": "18:20",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "17:15",
        "arrival_time": "19:05",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "17:40",
        "arrival_time": "19:30",
        "route_coordinates": [
            [11.2588, 75.7804],   # Bandadka
            [10.9982, 76.0458],   # Palakkad approach
            [10.7867, 76.6548],   # Kasaragod
        ],
    },

    # {
    #     "bus_id": "KL-14",
    #     "bus_name": "KSRTC",
    #     "from": "Bandadka",
    #     "to": "Kasaragod",
    #     "departure_time": "18:30",
    #     "arrival_time": "12:30",
    #     "route_coordinates": [
    #         [11.2588, 75.7804],
    #         [11.1085, 75.9874],
    #         [10.9982, 76.0458],
    #         [10.8350, 76.2710],
    #         [10.7867, 76.6548],
    #     ],
    # },

    # {
    #     "bus_id": "KL-14",
    #     "bus_name": "KSRTC",
    #     "from": "Bandadka",
    #     "to": "Kasaragod",
    #     "departure_time": "19:00",
    #     "arrival_time": "20:50",
    #     "route_coordinates": [
    #         [11.2588, 75.7804],
    #         [11.1085, 75.9874],
    #         [10.9982, 76.0458],
    #         [10.8350, 76.2710],
    #         [10.7867, 76.6548],
    #     ],
    # },

    # {
    #     "bus_id": "KL-14",
    #     "bus_name": "KSRTC",
    #     "from": "Bandadka",
    #     "to": "Kasaragod",
    #     "departure_time": "19:40",
    #     "arrival_time": "21:30",
    #     "route_coordinates": [
    #         [11.2588, 75.7804],
    #         [11.1085, 75.9874],
    #         [10.9982, 76.0458],
    #         [10.8350, 76.2710],
    #         [10.7867, 76.6548],
    #     ],
    # },


    # ── Route 2: Kasaragod → Bandadka ────────────────────────────────────────
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "05:50",
        "arrival_time": "07:40",
        "route_coordinates": [
            [10.7867, 76.6548],   # Kasaragod
            [10.5276, 76.2144],   # Chalakudy
            [9.9816,  76.2999],   # Bandadka

        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "08:45",
        "arrival_time": "10:35",   # Midnight crossover!
        "route_coordinates": [
            [10.7867, 76.6548],
            [10.6500, 76.4000],
            [10.5276, 76.2144],
            [10.2000, 76.3000],
            [9.9816,  76.2999],
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "09:10",
        "arrival_time": "11:00",
        "route_coordinates": [
            [10.7867, 76.6548],   # Kasaragod
            [10.5276, 76.2144],   # Chalakudy
            [9.9816,  76.2999],   # Bandadka

        ],
    },
    
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "10:40",
        "arrival_time": "12:30",   # Midnight crossover!
        "route_coordinates": [
            [10.7867, 76.6548],
            [10.6500, 76.4000],
            [10.5276, 76.2144],
            [10.2000, 76.3000],
            [9.9816,  76.2999],
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "16:00",
        "arrival_time": "17:50",
        "route_coordinates": [
            [10.7867, 76.6548],   # Kasaragod
            [10.5276, 76.2144],   # Chalakudy
            [9.9816,  76.2999],   # Bandadka

        ],
    },
    
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "18:30",
        "arrival_time": "20:20",   # Midnight crossover!
        "route_coordinates": [
            [10.7867, 76.6548],
            [10.6500, 76.4000],
            [10.5276, 76.2144],
            [10.2000, 76.3000],
            [9.9816,  76.2999],
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "20:00",
        "arrival_time": "21:50",
        "route_coordinates": [
            [10.7867, 76.6548],   # Kasaragod
            [10.5276, 76.2144],   # Chalakudy
            [9.9816,  76.2999],   # Bandadka

        ],
    },
    
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "20:20",
        "arrival_time": "22:10",   # Midnight crossover!
        "route_coordinates": [
            [10.7867, 76.6548],
            [10.6500, 76.4000],
            [10.5276, 76.2144],
            [10.2000, 76.3000],
            [9.9816,  76.2999],
        ],
    },

    # ── Route 3: Kanhangad→ Sullia ───────────────────────────────
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kanhangad",
        "to": "Sullia",
        "departure_time": "05:00",
        "arrival_time": "09:45",
        "route_coordinates": [
            [9.9816,  76.2999],   # Kanhangad

            [9.5916,  76.5222],   # Kottayam
            [8.8932,  76.6141],   # Kollam
            [8.5241,  76.9366],   # Sullia
        ],
    },

    
    # ── Route 4: Bandadka → Kanhangad ───────────────────────────────────────
    {
        "bus_id": "KL-14",
        "bus_name": "Akshaya",
        "from": "Bandadka",
        "to": "Kanhangad",
        "departure_time": "10:00",
        "arrival_time": "14:30",
        "route_coordinates": [
            [11.2588, 75.7804],
            [10.7867, 76.6548],
            [10.5276, 76.2144],
            [9.9816,  76.2999],
        ],
    },
    # ── Route 5: Sullia→ Bandadka (long haul) ──────────────────
    {
        "bus_id": "KL-14",
        "bus_name": "Guruji",
        "from": "Sullia",
        "to": "Bandadka",
        "departure_time": "21:00",
        "arrival_time": "06:30",   # Next morning!
        "route_coordinates": [
            [8.5241,  76.9366],
            [8.8932,  76.6141],
            [9.5916,  76.5222],
            [9.9816,  76.2999],
            [10.5276, 76.2144],
            [10.7867, 76.6548],
            [11.2588, 75.7804],
        ],
    },
]

result = buses_col.insert_many(sample_buses)
print(f"✅  Inserted {len(result.inserted_ids)} buses into MongoDB.")
print("   Collection: bus_tracker.buses")
