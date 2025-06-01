"""
GARDEN Sunflower API - Secured Version
Pattern detection and analysis for GARDEN ecosystem
"""
import json
from _auth import require_api_key, create_response

# GARDEN-specific patterns
PATTERNS = {
    "tool_cluster": {
        "name": "Tool Cluster",
        "description": "Groups of tools frequently used together",
        "query": "MATCH (u:User)-[:USES]->(t1:Tool), (u)-[:USES]->(t2:Tool) WHERE t1 <> t2 RETURN t1, t2, count(u) as users"
    },
    "user_journey": {
        "name": "User Journey",
        "description": "Common paths through GARDEN tools",
        "query": "MATCH path = (u:User)-[:STARTED_WITH]->(:Tool)-[:THEN_USED*]->(:Tool) RETURN path"
    },
    "fork_evolution": {
        "name": "Fork Evolution",  
        "description": "How projects evolve through forking",
        "query": "MATCH (p1:Project)-[:FORKED_TO]->(p2:Project) RETURN p1, p2"
    },
    "cognitive_alignment": {
        "name": "Cognitive Alignment",
        "description": "Which tools match which thinking patterns",
        "query": "MATCH (t:Tool)-[:IMPLEMENTS]->(p:Pattern) RETURN t, p"
    }
}

@require_api_key
def handler(request):
    """
    Handle Sunflower API requests with authentication
    """
    try:
        # Parse request body
        body = json.loads(request.body) if request.body else {}
        pattern_type = body.get('pattern')
        
        if not pattern_type:
            # Return available patterns
            result = {
                "patterns": [
                    {
                        "id": key,
                        "name": value["name"],
                        "description": value["description"]
                    }
                    for key, value in PATTERNS.items()
                ]
            }
        
        elif pattern_type in PATTERNS:
            # Mock pattern detection results
            pattern = PATTERNS[pattern_type]
            
            # Simulate pattern results based on type
            if pattern_type == "tool_cluster":
                result = {
                    "pattern": pattern["name"],
                    "clusters": [
                        {"tools": ["nodepad", "uploader"], "users": 15},
                        {"tools": ["explorer", "sunflower"], "users": 8},
                        {"tools": ["CIT_generator", "nodepad"], "users": 12}
                    ]
                }
            elif pattern_type == "cognitive_alignment":
                result = {
                    "pattern": pattern["name"],
                    "alignments": [
                        {"tool": "nodepad", "pattern": "grasshopper", "strength": 0.9},
                        {"tool": "explorer", "pattern": "grassroots", "strength": 0.95},
                        {"tool": "sunflower", "pattern": "sunflower", "strength": 1.0}
                    ]
                }
            else:
                result = {
                    "pattern": pattern["name"],
                    "message": "Pattern detection in progress"
                }
        
        else:
            return create_response({"error": "Pattern not found"}, 404)
            
        return create_response(result)
        
    except Exception as e:
        return create_response({"error": str(e)}, 500)
