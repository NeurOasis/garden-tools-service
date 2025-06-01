"""
GARDEN Tools Service Authentication
Provides API key protection for all endpoints
"""
import os
import json
from functools import wraps

# Get API key from environment variable
GARDEN_API_KEY = os.environ.get('GARDEN_API_KEY')

def require_api_key(f):
    """
    Decorator to require API key for endpoint access
    """
    @wraps(f)
    def decorated_function(request):
        # Get API key from headers
        api_key = request.headers.get('X-API-Key')
        
        # Allow OPTIONS requests for CORS
        if request.method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type, X-API-Key',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                }
            }
        
        # Check API key
        if not GARDEN_API_KEY:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'error': 'Server configuration error',
                    'message': 'API key not configured'
                })
            }
            
        if not api_key or api_key != GARDEN_API_KEY:
            return {
                'statusCode': 401,
                'body': json.dumps({
                    'error': 'Unauthorized',
                    'message': 'Valid API key required in X-API-Key header'
                }),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
            
        # Call the actual function
        return f(request)
    
    return decorated_function

def create_response(data, status_code=200):
    """
    Create a properly formatted API response
    """
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type, X-API-Key'
        },
        'body': json.dumps(data)
    }
