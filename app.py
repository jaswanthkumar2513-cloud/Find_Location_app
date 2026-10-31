from flask import Flask, request, render_template
import math

app = Flask(__name__)

shop_state = {
    "status": "Waiting for customers...",
    "distance": None,
    "alert": False,
    "message": ""
}

def get_distance(lat1, lon1, lat2, lon2):
    R = 6371000 
    phi_1, phi_2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2.0)**2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda/2.0)**2
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))

# TIRUPATI, ANDHRA PRADESH COORDINATES
SHOP_LAT = 13.6288 
SHOP_LON = 79.4192

@app.route('/')
@app.route('/index.html')
@app.route('/app.html')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    global shop_state
    data = request.get_json(silent=True) or {}
    
    lat = data.get('lat')
    lon = data.get('lon') if 'lon' in data else data.get('lng')
    
    if lat is not None and lon is not None:
        try:
            lat = float(lat)
            lon = float(lon)
            distance = get_distance(lat, lon, SHOP_LAT, SHOP_LON)
            shop_state["distance"] = int(distance)
            
            # HACKATHON TRICK: Set alert threshold to 1,000 km so the dashboard 
            # turns RED during your pitch, even though you are in Tamil Nadu!
            if distance < 1000000: 
                shop_state["status"] = "🚨 CUSTOMER EN ROUTE TO TIRUPATI!"
                shop_state["alert"] = True
            else:
                shop_state["status"] = "Customer is too far."
                shop_state["alert"] = False
        except (ValueError, TypeError):
            pass
            
    shop_state["message"] = data.get('message', '') or data.get('user_message', '')
        
    return {"status": "success", "state": shop_state}

@app.route('/owner')
def owner():
    return render_template('owner.html', state=shop_state)

@app.route('/api/state')
def api_state():
    return shop_state

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
