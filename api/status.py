"""GARDEN Tools Service Status API"""
import json

def handler(request, response):
    """Public status endpoint"""
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    return json.dumps({
        "status": "healthy",
        "service": "GARDEN Tools Service",
        "version": "1.0.0",
        "endpoints": {
            "/api/explorer": "Graph navigation (requires API key)",
            "/api/sunflower": "Pattern detection (requires API key)",
            "/api/status": "Health check (public)"
        }
    })
