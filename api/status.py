"""
GARDEN Tools Service Status API
Public health check endpoint (no auth required)
"""
import json
from _auth import create_response

def handler(request):
    """
    Public status endpoint for health checks
    No authentication required
    """
    return create_response({
        "status": "healthy",
        "service": "GARDEN Tools Service",
        "version": "1.0.0",
        "endpoints": {
            "/api/explorer": "Graph navigation (requires API key)",
            "/api/sunflower": "Pattern detection (requires API key)",
            "/api/status": "Health check (public)"
        },
        "authentication": "API key required in X-API-Key header"
    })
