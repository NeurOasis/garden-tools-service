"""
GARDEN Explorer API - Secured Version
Graph navigation and structure analysis for GARDEN ecosystem
"""
import json
from _auth import require_api_key, create_response

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
        },
        "users": {
            "type": "entity",
            "description": "GARDEN community members",
            "instances": ["Scott", "Dan", "Andrew", "Melissa"]
        }
    },
    "relationships": [
        {"from": "Scott", "to": "nodepad", "type": "CREATED"},
        {"from": "Dan", "to": "CIT_Framework", "type": "PIONEERED"},
        {"from": "nodepad", "to": "contexts", "type": "USES"}
    ]
}

@require_api_key
def handler(request):
    """
    Handle Explorer API requests with authentication
    """
    try:
        # Parse request body
        body = json.loads(request.body) if request.body else {}
        query_type = body.get('type', 'schema')
        
        if query_type == 'schema':
            # Return overall structure
            result = {
                "schema": {
                    "nodes": list(GARDEN_STRUCTURE["nodes"].keys()),
                    "relationships": ["CREATED", "USES", "DEPENDS_ON", "FORKED_FROM"]
                }
            }
        
        elif query_type == 'node':
            # Return specific node info
            node_name = body.get('node')
            if node_name in GARDEN_STRUCTURE["nodes"]:
                result = {
                    "node": node_name,
                    "data": GARDEN_STRUCTURE["nodes"][node_name]
                }
            else:
                return create_response({"error": "Node not found"}, 404)
        
        elif query_type == 'relationships':
            # Return relationships
            node_name = body.get('node')
            if node_name:
                related = [r for r in GARDEN_STRUCTURE["relationships"] 
                          if r["from"] == node_name or r["to"] == node_name]
                result = {"relationships": related}
            else:
                result = {"relationships": GARDEN_STRUCTURE["relationships"]}
        
        else:
            return create_response({"error": "Invalid query type"}, 400)
            
        return create_response(result)
        
    except Exception as e:
        return create_response({"error": str(e)}, 500)
