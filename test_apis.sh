#!/bin/bash

# GARDEN Tools API Test Script
echo "🚀 GARDEN Tools API Test Suite"
echo "================================"

API_KEY="cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f"
API_BASE="https://garden-tools-service.vercel.app/api"

echo ""
echo "🌱 Testing Status Endpoint..."
curl -s "${API_BASE}/status" | jq '.' > status_result.json
echo "Status result saved to status_result.json"

echo ""
echo "🔍 Testing Explorer API - Schema..."
curl -s -X POST "${API_BASE}/explorer" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{"type": "schema"}' | jq '.' > explorer_schema_result.json
echo "Explorer schema result saved to explorer_schema_result.json"

echo ""
echo "🔍 Testing Explorer API - Relationships..."
curl -s -X POST "${API_BASE}/explorer" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{"type": "relationships"}' | jq '.' > explorer_relationships_result.json
echo "Explorer relationships result saved to explorer_relationships_result.json"

echo ""
echo "🌻 Testing Sunflower API - List Patterns..."
curl -s -X POST "${API_BASE}/sunflower" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{}' | jq '.' > sunflower_patterns_result.json
echo "Sunflower patterns result saved to sunflower_patterns_result.json"

echo ""
echo "🌻 Testing Sunflower API - Tool Clusters..."
curl -s -X POST "${API_BASE}/sunflower" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d '{"pattern": "tool_cluster"}' | jq '.' > sunflower_tool_cluster_result.json
echo "Sunflower tool cluster result saved to sunflower_tool_cluster_result.json"

echo ""
echo "🎯 All tests complete! Results saved to individual JSON files."
echo "Check the current directory for the result files."
