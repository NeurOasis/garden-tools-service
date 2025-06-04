// GARDEN Tools API Test - Node.js Version
const GARDEN_API_KEY = 'cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f';
const API_BASE = 'https://garden-tools-service.vercel.app/api';

async function callGardenAPI(endpoint, data = {}) {
    const url = `${API_BASE}/${endpoint}`;
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-API-Key': GARDEN_API_KEY
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            const result = await response.json();
            return { success: true, data: result };
        } else {
            const error = await response.text();
            return { success: false, error: `${response.status}: ${error}` };
        }
    } catch (error) {
        return { success: false, error: error.message };
    }
}

async function testStatus() {
    try {
        const response = await fetch(`${API_BASE}/status`);
        if (response.ok) {
            const data = await response.json();
            return { success: true, data };
        } else {
            return { success: false, error: `Status: ${response.status}` };
        }
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { callGardenAPI, testStatus };
}

// For browser environment
if (typeof window !== 'undefined') {
    window.gardenAPI = { callGardenAPI, testStatus };
}
