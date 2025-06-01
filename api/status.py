from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "status": "healthy",
            "service": "GARDEN Tools Service",
            "version": "1.0.0",
            "endpoints": {
                "/api/explorer": "Graph navigation (requires API key)",
                "/api/sunflower": "Pattern detection (requires API key)",
                "/api/status": "Health check (public)"
            }
        }
        
        self.wfile.write(json.dumps(response).encode())
        return
