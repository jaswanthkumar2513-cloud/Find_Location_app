# Find Location App - Proximity & Check-In Tracker

A Flask-based proximity tracking web application that allows visitors to check in and share their location with a store owner dashboard in real time.

## Features

- **Visitor Check-In (`/`):** Real-time GPS location capture using the Geolocation API and interactive Leaflet map displaying:
  - Visitor's current location (Blue marker)
  - Sri Venkateswara Dress Shop in Tirupati, AP (Red marker)
  - Nearby landmark: Tirumala Temple (Green marker)
- **Live Owner Dashboard (`/owner`):** Real-time store terminal that calculates distance using the Haversine formula, displays distance in meters/kilometers, alerts when the customer is en route, and auto-syncs.
- **REST API (`/update_location`, `/api/state`):** Clean endpoints to receive coordinates and retrieve live shop state.

## Project Structure

```text
├── app.py              # Flask server and distance calculation logic
├── static/
│   └── app.js          # Landmark map helper functions
├── templates/
│   ├── index.html      # Customer visitor check-in & map interface
│   └── owner.html      # Real-time store owner terminal
└── .gitignore          # Git ignore rules
```

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install flask
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open in browser:**
   - Visitor Check-In: [http://localhost:5000/](http://localhost:5000/)
   - Owner Dashboard: [http://localhost:5000/owner](http://localhost:5000/owner)
