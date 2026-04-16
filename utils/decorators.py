import time
from functools import wraps

def retry(retries=3, delay=1):
    """
    A decorator that retries a function if it throws an exception.
    """
    def decorator(func):
        @wraps(func) # This preserves the original function's name and metadata
        def wrapper(*args, **kwargs):
            # The actual retry logic
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs) # Try to execute the original action
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            # If the loop finishes without returning, it means all retries failed
            raise Exception(f"Function {func.__name__} failed after {retries} attempts.")
        return wrapper
    return decorator
