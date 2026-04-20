from typing import Callable, Any


class RetryPolicy:
    def __init__(self, retries: int = 3):
        self.retries = retries

    def execute_with_retry(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        last_exception = None
        for attempt in range(self.retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
        raise last_exception
