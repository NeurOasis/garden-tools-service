"""GARDEN Sunflower API - Secured Version"""
import json
import os

GARDEN_API_KEY = os.environ.get('GARDEN_API_KEY')

PATTERNS = {
    "tool_cluster": {
        "name": "Tool Cluster",
        "description": "Groups of tools frequently used together"
    },
    "user_journey": {
        "name": "User Journey",
        "description": "Common paths through GARDEN tools"
    }
}

def handler(request, response):
    """Handle Sunflower API requests"""
    # Check API key
    api_key = request.headers.get('x-api-key')
    
    if request.method == 'OPTIONS':
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-API-Key'
        return
    
    if not api_key or api_key != GARDEN_API_KEY:
        response.status_code = 401
        return json.dumps({"error": "Unauthorized"})
    
    try:
        body = json.loads(request.body) if request.body else {}
        pattern_type = body.get('pattern')
        
        if not pattern_type:
            result = {"patterns": list(PATTERNS.keys())}
        else:
            result = {"pattern": pattern_type, "status": "Analysis complete"}
            
        response.status_code = 200
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return json.dumps(result)
        
    except Exception as e:
        response.status_code = 500
        return json.dumps({"error": str(e)})
