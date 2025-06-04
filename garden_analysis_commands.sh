curl -s -X POST "https://garden-tools-service.vercel.app/api/explorer" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f" \
  -d '{"type": "node", "node": "projects"}' > switch2_project_structure.json

curl -s -X POST "https://garden-tools-service.vercel.app/api/sunflower" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f" \
  -d '{"pattern": "cognitive_alignment"}' > switch2_cognitive_patterns.json

curl -s -X POST "https://garden-tools-service.vercel.app/api/sunflower" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f" \
  -d '{"pattern": "user_journey"}' > switch2_user_journey.json