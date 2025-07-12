# 0x02. Redis Basic

## Project Overview
This project is part of the ALX Backend Storage curriculum and focuses on learning the basics of Redis, a fast in-memory data store used as a database, cache, and message broker. The project involves implementing a `Cache` class to perform basic Redis operations, such as storing and retrieving data, counting method calls, storing call history, and implementing a web cache with access tracking. The project is designed to run on Ubuntu 18.04 LTS using Python 3.7 and adheres to the pycodestyle (version 2.5) style guide.


## Learning Objectives
- Learn how to use redis for basic operations (e.g., storing and retrieving strings, numbers, and bytes).
- Learn how to use redis as a simple cache

## Requirements
- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All of your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5)
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

### Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Use Redis in a container
Redis server is stopped by default - when you are starting a container, you should start it with: `service redis-server start`

## Directory Structure:
```
0x02-redis_basic/
├── exercise.py
├── web.py
├── main.py          # For testing Tasks 0-4
├── main_web.py     # Optional: For testing Task 5
└── README.md
```

## Tasks
### Task 0 (Writing strings to Redis):
- Implements `Cache` class with Redis client initialization
- `store` method generates random UUID key and stores data
- Type-annotated to accept str, bytes, int, or float

### Task 1 (Reading from Redis):
- Implements `get` method with optional conversion function
- Adds `get_str` and `get_int` convenience methods
- Handles None case when key doesn't exist
- Properly converts data back to original type

### Task 2 (Incrementing values):
- Implements `count_calls` decorator using Redis INCR
- Uses method's `__qualname__` for key
- Preserves original function metadata with functools.wraps

### Task 3 (Storing lists):
- Implements `call_history` decorator
- Stores inputs and outputs in separate Redis lists
- Uses RPUSH to append to lists
- Normalizes inputs using str()

### Task 4 (Retrieving lists):
- Implements `replay` function to show call history
- Uses LRANGE to get all inputs/outputs
- Zips inputs and outputs for formatted display

### Task 5 (Web cache and tracker):
- Implements `get_page` function with requests
- Uses decorator to track URL access counts
- Caches results with 10-second expiration using SETEX
- Stores access count in separate key


## main.py
- **Task 0:** Tests the `store` method by storing `b"hello"` and retrieving it with a direct Redis client to verify the key-value pair.
- **Task 1:** Tests the `get`, `get_str`, and `get_int` methods using the provided TEST_CASES dictionary to ensure proper type conversion.
- **Task 2:** Tests the `count_calls` decorator by calling `store` multiple times and checking the incrementing count stored in Redis under `cache.store.__qualname__.`
- **Task 3:** Tests the `call_history` decorator by storing inputs and outputs in Redis lists and printing them.
- **Task 4:** Tests the `replay` function to display the history of calls to `cache.store`.


## Setup Instructions
**1. Install Redis:**
```
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

**2. Run Redis in a Container:**
```
service redis-server start
```

**3. Install Python Dependencies:**
```
pip3 install redis requests
```

**4. Run Tests:**
- Test Tasks 0-4 using `python3 main.py`.
- Test Task 5 by creating a test script or using a URL like `http://slowwly.robertomurray.co.uk` to verify caching.

## Notes
- Ensure all Python files are executable (`chmod +x *.py`).
- Ensure Redis is installed and running (`service redis-server start in a container`) and the required Python packages are installed (`pip3 install redis requests` ).
- Test the web cache (Task 5) using a slow-responding URL like `http://slowwly.robertomurray.co.uk` to verify caching behavior.
