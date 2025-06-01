# GARDEN Tools Service

Always-on microservices for GARDEN's Python-based tools.

## Architecture

This repository contains serverless functions that provide API access to GARDEN's advanced tools:

- **Explorer**: Graph-based navigation and visualization
- **Sunflower**: Pattern detection and analysis
- **Module Generators**: Schema generation tools (coming soon)

## Deployment

Automatically deployed to Vercel on push to main branch.

## API Endpoints

### Status
- `GET /` - Service status and available endpoints

### Explorer API
- `POST /api/explorer` - Graph exploration queries

Example queries:
```json
// Get schema
{"type": "schema"}

// Get node details
{"type": "node", "id": "nodepad"}

// Search nodes
{"type": "search", "term": "pattern"}

// Find path between nodes
{"type": "path", "start": "Scott", "end": "Dan"}
```

### Sunflower API
- `POST /api/sunflower` - Pattern detection queries

Example queries:
```json
// Get all patterns
{"pattern": "all"}

// Detect tool clusters
{"pattern": "tool_clusters"}

// Analyze user journeys
{"pattern": "user_journeys"}

// Check cognitive alignment
{"pattern": "cognitive_alignment"}
```

## Development

```bash
# Install Vercel CLI
npm install -g vercel

# Run locally
vercel dev

# Deploy to production
vercel --prod
```

## Integration with GARDEN Core

These tools are referenced in the main GARDEN repository via MOCI manifests. The core repository maintains awareness of these services without including the actual code.

## Token Efficiency

By separating these tools into microservices:
- GARDEN core stays under 30% project knowledge
- Tools can be updated independently
- Claude maintains full awareness via compressed manifests
- Zero bloat in the main repository

## Contributing

1. Fork this repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

Part of the GARDEN ecosystem - see main repository for license details.
