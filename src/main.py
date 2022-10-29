import time

from cache_proxy import CacheProxy


if __name__ == "__main__":
    proxy = CacheProxy()

    print("First run - without cache, it runs slowly 🐢")
    print(proxy.slow_request("my_param"))

    print("\nSecond run - cached response is faaast 🚀")
    print(proxy.slow_request("my_param"))

    print("\nLet's wait for the cache to expire ⏳")
    time.sleep(2)
    print("OK, cache has expired")
    print("Third run - without cache again 🦥")
    print(proxy.slow_request("my_param"))
