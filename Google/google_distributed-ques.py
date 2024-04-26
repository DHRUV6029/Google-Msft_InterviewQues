# Questions were in parts

# Implement given interface having one method
# Write a class/method to execute above method only once/second
# after implementing above 2, we had 15 min so he asked, for given n, we should allow n requests/sec.
# Overall it was variation of Rate Limiter.

from queue import Queue
import threading
import time

class RateLimitedMethod:
    def execute(self):
        pass

class RateLimiter:
    last_executed_time = 0
    request_queue = Queue()
    lock = threading.Lock()

    @staticmethod
    def execute_once_per_second(method: RateLimitedMethod):
        current_time = time.time()
        with RateLimiter.lock:
            if RateLimiter.last_executed_time == 0 or current_time - RateLimiter.last_executed_time >= 1:
                method.execute()
                RateLimiter.last_executed_time = current_time

    @staticmethod
    def execute_n_requests_per_second(method: RateLimitedMethod, n: int):
        current_time = time.time()
        with RateLimiter.lock:
            while not RateLimiter.request_queue.empty() and current_time - RateLimiter.request_queue.queue[0] >= 1:
                RateLimiter.request_queue.get()
            if RateLimiter.request_queue.qsize() < n:
                method.execute()
                RateLimiter.request_queue.put(current_time)

# Example usage
class YourMethod(RateLimitedMethod):
    def execute(self):
        print("Executing method...")

# Usage
if __name__ == "__main__":
    method = YourMethod()
    for _ in range(5):
        RateLimiter.execute_n_requests_per_second(method , 5)
        time
        RateLimiter.execute_n_requests_per_second(method , 5)
        
        
