#!/usr/bin/env python3
"""
Web cache and tracker module
"""
import redis
import requests
from typing import Callable
from functools import wraps

redis_client = redis.Redis()

def track_url_access(method: Callable) -> Callable:
    """Decorator to track URL access count and cache results"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function for tracking and caching"""
        redis_client = redis.Redis()
        
        # Increment access count
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        
        # Check cache
        cache_key = f"cache:{url}"
        cached_content = redis_client.get(cache_key)
        
        if cached_content:
            return cached_content.decode("utf-8")
        
        # Get content and cache it
        content = method(url)
        redis_client.setex(cache_key, 10, content)
        return content
    
    return wrapper


@track_url_access
def get_page(url: str) -> str:
    # Count how many times the URL was accessed
    redis_client.incr(f"count:{url}")

    # Try to get cached version
    cached = redis_client.get(url)
    if cached:
        return cached.decode("utf-8")

    """Get HTML content of a URL"""
    response = requests.get(url)
    redis_client.setex(url, 10, response.text)
    return response.text
