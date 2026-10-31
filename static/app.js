/* global L, map */
// Function to add local landmarks to the Leaflet map
function addLandmarks(mapInstance) {
    const targetMap = mapInstance || (typeof map !== 'undefined' ? map : (typeof window !== 'undefined' ? window.map : null));
    const leaflet = typeof L !== 'undefined' ? L : (typeof window !== 'undefined' ? window.L : null);
    if (!leaflet || !targetMap) return null;

    // Green pin for a famous local landmark (e.g., Tirumala Temple)
    var landmarkIcon = leaflet.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34]
    });

    return leaflet.marker([13.6833, 79.3475], { icon: landmarkIcon })
        .addTo(targetMap)
        .bindPopup("<b>Nearby Landmark:</b><br>Tirumala Temple");
}

// Auto-run safely if a global map instance is already defined
if (typeof map !== 'undefined' && map) {
    addLandmarks(map);
} else if (typeof window !== 'undefined' && window.map) {
    addLandmarks(window.map);
}
