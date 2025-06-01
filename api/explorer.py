"""GARDEN Explorer API - Secured Version"""
import json
import os

GARDEN_API_KEY = os.environ.get('GARDEN_API_KEY')

# Mock data representing GARDEN structure
GARDEN_STRUCTURE = {
    "nodes": {
        "contexts": {
            "type": "directory",
            "description": "Context Initialization Templates",
            "children": ["CIT_Personal", "CIT_Project", "CIT_Framework"]
        },
        "toolshed": {
            "type": "directory", 
            "description": "GARDEN tools and utilities",
            "children": ["nodepad", "uploader", "explorer", "sunflower"]
        }
    },
    "relationships": [
        {"from": "Scott", "to": "nodepad", "type": "CREATED"},
        {"from": "nodepad", "to": "contexts", "type": "USES"}
    ]
}

def handler(request, response):
    """Handle Explorer API requests"""
    # Check API key
    api_key = request.headers.get('x-api-key')
    
    if request.method == 'OPTIONS':
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-API-Key'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        return
    
    if not api_key or api_key != GARDEN_API_KEY:
        response.status_code = 401
        return json.dumps({"error": "Unauthorized", "message": "Valid API key required"})
    
    try:
        body = json.loads(request.body) if request.body else {}
        query_type = body.get('type', 'schema')
        
        if query_type == 'schema':
            result = {
                "schema": {
                    "nodes": list(GARDEN_STRUCTURE["nodes"].keys()),
                    "relationships": ["CREATED", "USES", "DEPENDS_ON", "FORKED_FROM"]
                }
            }
        else:
            result = {"message": "Query type not implemented"}
            
        response.status_code = 200
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return json.dumps(result)
        
    except Exception as e:
        response.status_code = 500
        return json.dumps({"error": str(e)})
