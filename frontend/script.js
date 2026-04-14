/**
 * BusTrack Kerala — Frontend Logic
 * =================================
 * Responsibilities:
 *   1. Fetch location list from backend and populate dropdowns
 *   2. Search buses and render bus cards
 *   3. Calculate travel time from departure/arrival strings
 *   4. Open map modal and animate bus marker along route
 */

// ── Configuration ────────────────────────────────────────────────────────────
// Change this if your Flask server runs on a different port or host

const API_BASE = "";

// ── DOM References ─────────────────────────────────────────────────────────
const fromSelect     = document.getElementById("from-select");
const toSelect       = document.getElementById("to-select");
const swapBtn        = document.getElementById("swap-btn");
const searchBtn      = document.getElementById("search-btn");
const spinner        = document.getElementById("spinner");
const resultsSection = document.getElementById("results-section");
const busGrid        = document.getElementById("bus-grid");
const resultsTitle   = document.getElementById("results-title");
const resultsCount   = document.getElementById("results-count");
const errorMsg       = document.getElementById("error-msg");

// Map / Modal
const modalOverlay   = document.getElementById("modal-overlay");
const modalTitle     = document.getElementById("modal-title");
const modalClose     = document.getElementById("modal-close");

// ── Leaflet Map State ──────────────────────────────────────────────────────
let leafletMap       = null;   // Leaflet map instance
let busMarker        = null;   // Animated bus marker
let animationTimer   = null;   // setInterval reference for animation


// ═══════════════════════════════════════════════════════════════════════════
// 1. LOAD LOCATIONS ON PAGE READY
// ═══════════════════════════════════════════════════════════════════════════
async function loadLocations() {
  try {
    const response = await fetch(`${API_BASE}/routes`);
    if (!response.ok) throw new Error("Network response was not OK");

    const data = await response.json();
    const locations = data.locations; // e.g. ["Ernakulam", "Kozhikode", ...]

    // Populate both dropdowns with the same location list
    [fromSelect, toSelect].forEach(sel => {
      // Clear the "Loading…" placeholder
      sel.innerHTML = '<option value="">— Select location —</option>';

      locations.forEach(loc => {
        const opt = document.createElement("option");
        opt.value = loc;
        opt.textContent = loc;
        sel.appendChild(opt);
      });

      sel.disabled = false; // enable after data is ready
    });

    enableSearchIfReady();
  } catch (err) {
    showError("Could not load locations. Is the Flask server running?");
    console.error("loadLocations error:", err);
  }
}


// ═══════════════════════════════════════════════════════════════════════════
// 2. SEARCH BUSES
// ═══════════════════════════════════════════════════════════════════════════
async function searchBuses() {
  const from = fromSelect.value.trim();
  const to   = toSelect.value.trim();

  // Basic validation
  clearError();
  if (!from || !to) { showError("Please select both From and To locations."); return; }
  if (from === to)  { showError("From and To locations must be different.");  return; }

  // Show spinner, hide old results
  showSpinner(true);
  hideResults();

  try {
    const url = `${API_BASE}/buses?from=${encodeURIComponent(from)}&to=${encodeURIComponent(to)}`;
    const response = await fetch(url);
    if (!response.ok) throw new Error(`Server returned ${response.status}`);

    const data = await response.json();
    renderBusCards(data.buses || [], from, to);
  } catch (err) {
    showError("Failed to fetch buses. Please try again.");
    console.error("searchBuses error:", err);
  } finally {
    showSpinner(false);
  }
}


// ═══════════════════════════════════════════════════════════════════════════
// 3. TRAVEL TIME CALCULATION (JavaScript — preferred over backend)
// ═══════════════════════════════════════════════════════════════════════════
/**
 * calcTravelTime("22:00", "00:30") → "2h 30m"
 * Handles midnight crossover by checking if diff is negative,
 * then adding 24 * 60 minutes.
 *
 * @param {string} dep  - departure in "HH:MM" format
 * @param {string} arr  - arrival in "HH:MM" format
 * @returns {string}    - e.g. "3h 45m" or "0h 20m"
 */
function calcTravelTime(dep, arr) {
  // Parse hours and minutes
  const [dh, dm] = dep.split(":").map(Number);
  const [ah, am] = arr.split(":").map(Number);

  // Convert to total minutes since midnight
  const depMins = dh * 60 + dm;
  const arrMins = ah * 60 + am;

  // Raw difference (may be negative if crossing midnight)
  let diffMins = arrMins - depMins;

  // If negative (arrival is on the next day), add 24 hours in minutes
  if (diffMins < 0) diffMins += 24 * 60;

  const hours   = Math.floor(diffMins / 60);
  const minutes = diffMins % 60;

  // e.g. "2h 30m" or "0h 45m"
  return `${hours}h ${String(minutes).padStart(2, "0")}m`;
}


// ═══════════════════════════════════════════════════════════════════════════
// 4. RENDER BUS CARDS
// ═══════════════════════════════════════════════════════════════════════════
function renderBusCards(buses, from, to) {
  busGrid.innerHTML = ""; // clear previous cards

  // Update header info
  resultsTitle.textContent = `${from} → ${to}`;
  resultsCount.textContent = `${buses.length} bus${buses.length !== 1 ? "es" : ""} found`;

  if (buses.length === 0) {
    busGrid.innerHTML = `
      <div class="no-results">
        <div class="no-icon">🔍</div>
        <p>No buses found for this route. Try a different combination.</p>
      </div>`;
  } else {
    buses.forEach((bus, idx) => {
      // Calculate travel time in JS (not relying on backend value)
      const travelTime = calcTravelTime(bus.departure_time, bus.arrival_time);

      const card = document.createElement("div");
      card.className = "bus-card";
      card.style.animationDelay = `${idx * 0.07}s`;

      card.innerHTML = `
        <div class="card-header">
          <div>
            <span class="bus-id-badge">${escHtml(bus.bus_id)}</span>
            <div class="bus-name">${escHtml(bus.bus_name)}</div>
          </div>
        </div>

        <div class="timing-row">
          <div class="time-block">
            <div class="time-label">Departure</div>
            <div class="time-value time-dep">${escHtml(bus.departure_time)}</div>
          </div>

          <div class="time-divider">
            <div class="divider-line"></div>
            <div class="divider-duration">⏱ ${travelTime}</div>
          </div>

          <div class="time-block">
            <div class="time-label">Arrival</div>
            <div class="time-value time-arr">${escHtml(bus.arrival_time)}</div>
          </div>
        </div>

        <button class="track-btn" data-bus-id="${escHtml(bus.bus_id)}" data-bus-name="${escHtml(bus.bus_name)}">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="3"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2
              m-4.22-7.78-1.42 1.42M7.64 16.36l-1.42 1.42m12.73 0-1.42-1.42
              M7.64 7.64 6.22 6.22"/>
          </svg>
          Track Bus
        </button>
      `;

      // Attach track button listener
      card.querySelector(".track-btn").addEventListener("click", () => {
        openTrackModal(bus.bus_id, bus.bus_name);
      });

      busGrid.appendChild(card);
    });
  }

  showResults();
}


// ═══════════════════════════════════════════════════════════════════════════
// 5. MAP / TRACKING
// ═══════════════════════════════════════════════════════════════════════════
async function openTrackModal(busId, busName) {
  clearError();
  modalTitle.textContent = busName;

  // Show modal
  modalOverlay.hidden = false;
  document.body.style.overflow = "hidden"; // prevent background scroll

  try {
    // Fetch route coordinates from backend
    const response = await fetch(`${API_BASE}/track/${encodeURIComponent(busId)}`);
    if (!response.ok) throw new Error(`Track API returned ${response.status}`);

    const data = await response.json();
    const coords = data.coordinates || []; // array of [lat, lng]

    if (coords.length < 2) {
      showError("Not enough coordinates to display the route.");
      return;
    }

    initMap(coords, busName);
  } catch (err) {
    showError("Could not load route. Check the backend.");
    console.error("openTrackModal error:", err);
  }
}

/**
 * Initialise or reinitialise the Leaflet map with the given coordinates.
 * Draws the polyline route and animates the bus marker along it.
 */
function initMap(coords, busName) {
  // If map already exists, remove it so we can re-init cleanly
  if (leafletMap) {
    clearInterval(animationTimer);
    leafletMap.remove();
    leafletMap = null;
  }

  // Centre the map on the mid-point of the route
  const midIdx = Math.floor(coords.length / 2);
  const centre = coords[midIdx];

  leafletMap = L.map("map", { zoomControl: true }).setView(centre, 8);

  // OpenStreetMap tiles
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "© OpenStreetMap contributors",
    maxZoom: 18,
  }).addTo(leafletMap);

  // ── Draw route polyline ──────────────────────────────────────────────
  const polyline = L.polyline(coords, {
    color: "#f5a623",
    weight: 4,
    opacity: 0.85,
    dashArray: "8, 6",
  }).addTo(leafletMap);

  leafletMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });

  // ── Origin marker (green) ────────────────────────────────────────────
  const originIcon = L.divIcon({
    html: `<div style="
      width:14px;height:14px;border-radius:50%;
      background:#22c55e;border:2px solid #fff;
      box-shadow:0 0 8px #22c55e;">
    </div>`,
    iconSize: [14, 14], iconAnchor: [7, 7],
  });
  L.marker(coords[0], { icon: originIcon })
   .addTo(leafletMap)
   .bindPopup("🟢 Origin");

  // ── Destination marker (red) ─────────────────────────────────────────
  const destIcon = L.divIcon({
    html: `<div style="
      width:14px;height:14px;border-radius:50%;
      background:#ef4444;border:2px solid #fff;
      box-shadow:0 0 8px #ef4444;">
    </div>`,
    iconSize: [14, 14], iconAnchor: [7, 7],
  });
  L.marker(coords[coords.length - 1], { icon: destIcon })
   .addTo(leafletMap)
   .bindPopup("🔴 Destination");

  // ── Animated bus marker ──────────────────────────────────────────────
  const busIcon = L.divIcon({
    html: `<div style="
      font-size:24px;line-height:1;
      filter:drop-shadow(0 2px 4px rgba(0,0,0,0.6));">🚌</div>`,
    iconSize: [28, 28], iconAnchor: [14, 20],
  });
  busMarker = L.marker(coords[0], { icon: busIcon })
    .addTo(leafletMap)
    .bindPopup(`🚌 ${busName}`);

  // Animate the marker to step through coords with interpolation
  animateBus(coords);
}

/**
 * Smoothly move the bus marker through each coordinate segment.
 * Each "segment" is split into STEPS sub-steps for fluid animation.
 */
function animateBus(coords) {
  const STEPS = 60;        // interpolation steps per segment
  const INTERVAL = 60;     // ms between steps (≈ 60fps)

  let segIdx  = 0;  // which segment (pair of coords) we are on
  let stepIdx = 0;  // which interpolation step within that segment

  clearInterval(animationTimer);

  animationTimer = setInterval(() => {
    if (segIdx >= coords.length - 1) {
      // Reached end — loop back to start after a short pause
      segIdx  = 0;
      stepIdx = 0;
      busMarker.setLatLng(coords[0]);
      return;
    }

    const [lat1, lng1] = coords[segIdx];
    const [lat2, lng2] = coords[segIdx + 1];

    // Linear interpolation (lerp) between two points
    const t    = stepIdx / STEPS;
    const lat  = lat1 + (lat2 - lat1) * t;
    const lng  = lng1 + (lng2 - lng1) * t;

    busMarker.setLatLng([lat, lng]);

    stepIdx++;
    if (stepIdx > STEPS) {
      stepIdx = 0;
      segIdx++;
    }
  }, INTERVAL);
}


// ═══════════════════════════════════════════════════════════════════════════
// 6. UTILITY HELPERS
// ═══════════════════════════════════════════════════════════════════════════

/** Escape HTML to prevent XSS when inserting user/API data into innerHTML */
function escHtml(str) {
  const div = document.createElement("div");
  div.textContent = String(str);
  return div.innerHTML;
}

function showSpinner(visible) {
  spinner.hidden = !visible;
}

function showResults() {
  resultsSection.hidden = false;
}

function hideResults() {
  resultsSection.hidden = true;
}

function showError(msg) {
  errorMsg.textContent = msg;
}

function clearError() {
  errorMsg.textContent = "";
}

/** Enable the Search button only when both dropdowns have a value */
function enableSearchIfReady() {
  fromSelect.addEventListener("change", toggleSearchBtn);
  toSelect.addEventListener("change",   toggleSearchBtn);
}

function toggleSearchBtn() {
  const ready = fromSelect.value && toSelect.value;
  searchBtn.disabled = !ready;
}


// ═══════════════════════════════════════════════════════════════════════════
// 7. EVENT LISTENERS
// ═══════════════════════════════════════════════════════════════════════════

// Search button click
searchBtn.addEventListener("click", searchBuses);

// Allow pressing Enter in either dropdown to trigger search
[fromSelect, toSelect].forEach(sel => {
  sel.addEventListener("keydown", e => {
    if (e.key === "Enter") searchBuses();
  });
});

// Swap From ↔ To values
swapBtn.addEventListener("click", () => {
  const temp = fromSelect.value;
  fromSelect.value = toSelect.value;
  toSelect.value   = temp;
  toggleSearchBtn();
});

// Close modal
modalClose.addEventListener("click", closeModal);

// Close modal when clicking the dark overlay
modalOverlay.addEventListener("click", e => {
  if (e.target === modalOverlay) closeModal();
});

// Close modal with Escape key
document.addEventListener("keydown", e => {
  if (e.key === "Escape" && !modalOverlay.hidden) closeModal();
});

function closeModal() {
  modalOverlay.hidden = true;
  document.body.style.overflow = "";

  // Stop animation and clean up map
  clearInterval(animationTimer);
  if (leafletMap) {
    leafletMap.remove();
    leafletMap = null;
  }
}


// ═══════════════════════════════════════════════════════════════════════════
// 8. INIT — Run when page loads
// ═══════════════════════════════════════════════════════════════════════════
loadLocations();
