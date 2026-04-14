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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka  
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
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
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "18:30",
        "arrival_time": "12:30",
        "route_coordinates": [
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "19:00",
        "arrival_time": "20:50",
        "route_coordinates": [
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
        ],
    },

    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Bandadka",
        "to": "Kasaragod",
        "departure_time": "19:40",
        "arrival_time": "21:30",
        "route_coordinates": [
            [12.4996, 74.9869],   # Kasaragod
            [12.4760, 75.0005],   # Vidyanagar
            [12.4555, 75.0300],   # Chengala
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4200, 75.1000],   # Melparamba
            [12.4405, 75.1705],   # Poinachi
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4800, 75.2300],   # Karadka
            [12.4850, 75.2400],   # Kuttikol
            [12.4955, 75.2550],   # Padupp
            [12.50136, 75.26871]  # Bandadka
        ],
    },


    # ── Route 2: Kasaragod → Bandadka ────────────────────────────────────────
    
    {
        "bus_id": "KL-14",
        "bus_name": "KSRTC",
        "from": "Kasaragod",
        "to": "Bandadka",
        "departure_time": "05:50",
        "arrival_time": "07:40",
        "route_coordinates": [
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod

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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod
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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod
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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod
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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod

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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod
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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod
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
            [12.50136, 75.26871], # Bandadka
            [12.4955, 75.2550],   # Padupp
            [12.4850, 75.2400],   # Kuttikol
            [12.4800, 75.2300],   # Karadka
            [12.4705, 75.2150],   # Kundamkuzhy
            [12.4650, 75.2050],   # Kanhiradukkam
            [12.4550, 75.1900],   # Koliyadukkam
            [12.4405, 75.1705],   # Poinachi
            [12.4200, 75.1000],   # Melparamba
            [12.4305, 75.0700],   # Cherkala Junction
            [12.4555, 75.0300],   # Chengala
            [12.4760, 75.0005],   # Vidyanagar
            [12.4996, 74.9869]    # Kasaragod
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
            # [9.9816,  76.2999],   

            # [9.5916,  76.5222],    
            # [8.8932,  76.6141],  
            # [8.5241,  76.9366],    
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
            # [11.2588, 75.7804],
            # [10.7867, 76.6548],
            # [10.5276, 76.2144],
            # [9.9816,  76.2999],
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
            # [8.5241,  76.9366],
            # [8.8932,  76.6141],
            # [9.5916,  76.5222],
            # [9.9816,  76.2999],
            # [10.5276, 76.2144],
            # [10.7867, 76.6548],
            # [11.2588, 75.7804],
        ],
    },
]

result = buses_col.insert_many(sample_buses)
print(f"✅  Inserted {len(result.inserted_ids)} buses into MongoDB.")
print("   Collection: bus_tracker.buses")
