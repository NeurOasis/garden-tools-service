#!/bin/bash

API_KEY="cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f"
API_BASE="https://garden-tools-service.vercel.app/api"

echo "🔍 Querying GARDEN Explorer for strategic project structure..."
curl -s -X POST "${API_BASE}/explorer" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{"type": "node", "node": "projects"}' > switch2_project_structure.json

echo "🌻 Analyzing optimal cognitive patterns for strategic planning..."
curl -s -X POST "${API_BASE}/sunflower" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{"pattern": "cognitive_alignment"}' > switch2_cognitive_patterns.json

echo "🌻 Detecting tool clusters for strategic execution..."
curl -s -X POST "${API_BASE}/sunflower" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{"pattern": "user_journey"}' > switch2_user_journey.json

echo "✅ GARDEN analysis complete for Switch 2 project"
