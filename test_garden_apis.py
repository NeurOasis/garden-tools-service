#!/usr/bin/env python3
"""
GARDEN Tools API Test Script
Tests the Explorer and Sunflower APIs and saves results locally
"""

import requests
import json
import os
from datetime import datetime

# API Configuration
GARDEN_API_KEY = 'cdfc80571bc5c228d8171c2b00b5eff8575c550b991392eebb0e68928949186f'
API_BASE = 'https://garden-tools-service.vercel.app/api'

def call_garden_api(endpoint, data=None):
    """Make authenticated API call to GARDEN service"""
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': GARDEN_API_KEY
    }
    
    url = f"{API_BASE}/{endpoint}"
    print(f"🔗 Calling: {url}")
    print(f"📦 Data: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(url, json=data or {}, headers=headers)
        print(f"📊 Status: {response.status_code}")
        
        if response.ok:
            result = response.json()
            print(f"✅ Success!")
            return result
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"🚨 Exception: {str(e)}")
        return None

def test_status():
    """Test the public status endpoint"""
    print("\n🌱 Testing Status Endpoint...")
    try:
        response = requests.get(f"{API_BASE}/status")
        if response.ok:
            result = response.json()
            print("✅ Status endpoint working!")
            print(json.dumps(result, indent=2))
            return result
        else:
            print(f"❌ Status check failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"🚨 Status check exception: {str(e)}")
        return None

def test_explorer():
    """Test Explorer API endpoints"""
    print("\n🔍 Testing Explorer API...")
    
    results = {}
    
    # Test schema
    print("\n--- Getting Schema ---")
    schema = call_garden_api('explorer', {'type': 'schema'})
    if schema:
        results['schema'] = schema
    
    # Test node info
    print("\n--- Getting Node Info ---")
    node_info = call_garden_api('explorer', {'type': 'node', 'node': 'contexts'})
    if node_info:
        results['node_contexts'] = node_info
    
    # Test relationships
    print("\n--- Getting Relationships ---")
    relationships = call_garden_api('explorer', {'type': 'relationships'})
    if relationships:
        results['relationships'] = relationships
    
    return results

def test_sunflower():
    """Test Sunflower API endpoints"""
    print("\n🌻 Testing Sunflower API...")
    
    results = {}
    
    # Test pattern list
    print("\n--- Getting Pattern List ---")
    patterns = call_garden_api('sunflower', {})
    if patterns:
        results['patterns'] = patterns
    
    # Test specific patterns
    pattern_types = ['tool_cluster', 'user_journey', 'cognitive_alignment']
    
    for pattern in pattern_types:
        print(f"\n--- Testing Pattern: {pattern} ---")
        pattern_result = call_garden_api('sunflower', {'pattern': pattern})
        if pattern_result:
            results[f'pattern_{pattern}'] = pattern_result
    
    return results

def save_results(results, filename):
    """Save results to local file"""
    timestamp = datetime.now().isoformat()
    output = {
        'timestamp': timestamp,
        'results': results
    }
    
    filepath = f"/Users/scottloeb/Desktop/GitHub/neuroasis/garden-tools-service/{filename}"
    with open(filepath, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Results saved to: {filepath}")

def main():
    """Run all API tests"""
    print("🚀 GARDEN Tools API Test Suite")
    print("=" * 50)
    
    all_results = {}
    
    # Test status
    status_result = test_status()
    if status_result:
        all_results['status'] = status_result
    
    # Test Explorer
    explorer_results = test_explorer()
    if explorer_results:
        all_results['explorer'] = explorer_results
    
    # Test Sunflower
    sunflower_results = test_sunflower()
    if sunflower_results:
        all_results['sunflower'] = sunflower_results
    
    # Save results
    save_results(all_results, 'api_test_results.json')
    
    print("\n🎯 Test Summary:")
    print(f"Status: {'✅' if 'status' in all_results else '❌'}")
    print(f"Explorer: {'✅' if 'explorer' in all_results else '❌'}")
    print(f"Sunflower: {'✅' if 'sunflower' in all_results else '❌'}")
    
    return all_results

if __name__ == "__main__":
    results = main()
