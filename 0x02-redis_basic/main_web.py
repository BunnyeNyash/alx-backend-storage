#!/usr/bin/env python3
"""
Test file for web.py
"""
from web import get_page, redis_client

# Initialize Redis client for testing
redis_client = redis.Redis(decode_responses=False)

url = "http://slowwly.robertomurray.co.uk/delay/2000/url/http://example.com"
print(get_page(url))  # First call: fetches and caches
print(get_page(url))  # Second call: should return cached content
print(redis_client.get(f"count:{url}").decode("utf-8"))  # Should print "2"
