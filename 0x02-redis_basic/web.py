#!/usr/bin/env python3
"""
Web cache and tracker module
"""
import redis
import requests
from typing import Callable
from functools import wraps


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
    """Get HTML content of a URL"""
    response = requests.get(url)
    return response.text
