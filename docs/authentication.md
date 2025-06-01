# GARDEN Tools Service - Secure API Test

## Testing with Authentication

### 1. Set up your API key in Vercel:
```bash
vercel env add GARDEN_API_KEY production
# Enter your secret key when prompted
```

### 2. Test with curl:
```bash
# Test without API key (should fail)
curl -X POST https://your-app.vercel.app/api/explorer \
  -H "Content-Type: application/json" \
  -d '{"type": "schema"}'

# Test with API key (should work)
curl -X POST https://your-app.vercel.app/api/explorer \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-secret-key-here" \
  -d '{"type": "schema"}'
```

### 3. JavaScript client example:
```javascript
const GARDEN_API_KEY = 'your-secret-key-here';
const API_BASE = 'https://your-app.vercel.app/api';

async function callGardenAPI(endpoint, data) {
  const response = await fetch(`${API_BASE}/${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': GARDEN_API_KEY
    },
    body: JSON.stringify(data)
  });
  
  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }
  
  return response.json();
}

// Example usage
const schema = await callGardenAPI('explorer', { type: 'schema' });
const patterns = await callGardenAPI('sunflower', {});
```

### 4. Python client example:
```python
import requests

GARDEN_API_KEY = 'your-secret-key-here'
API_BASE = 'https://your-app.vercel.app/api'

def call_garden_api(endpoint, data=None):
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': GARDEN_API_KEY
    }
    
    response = requests.post(
        f"{API_BASE}/{endpoint}",
        json=data or {},
        headers=headers
    )
    
    response.raise_for_status()
    return response.json()

# Example usage
schema = call_garden_api('explorer', {'type': 'schema'})
patterns = call_garden_api('sunflower')
```

## Security Best Practices

1. **Never commit API keys** - Use environment variables
2. **Rotate keys regularly** - Change them every 90 days
3. **Use HTTPS only** - Vercel provides this automatically
4. **Monitor usage** - Check Vercel logs for unauthorized attempts
5. **Limit scope** - Create different keys for different environments

## Setting Environment Variables in Vercel

### Via Dashboard:
1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add `GARDEN_API_KEY` with your secret value
4. Select which environments (Production/Preview/Development)

### Via CLI:
```bash
vercel env add GARDEN_API_KEY production
vercel env add GARDEN_API_KEY preview
```

## Multiple API Keys (Advanced)

For different access levels, you can use multiple keys:

```python
# In your Vercel environment variables
GARDEN_API_KEY_ADMIN=super-secret-admin-key
GARDEN_API_KEY_READ=read-only-key
GARDEN_API_KEY_WRITE=write-access-key

# In your auth code
PERMISSION_LEVELS = {
    os.environ.get('GARDEN_API_KEY_ADMIN'): ['read', 'write', 'admin'],
    os.environ.get('GARDEN_API_KEY_READ'): ['read'],
    os.environ.get('GARDEN_API_KEY_WRITE'): ['read', 'write']
}
```
