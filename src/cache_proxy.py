from cache_manager import CacheManager
from processor import Processor


class CacheProxy(Processor):
    def __init__(self) -> None:
        self.__processor = Processor()
        self.__cache = CacheManager()

    def slow_request(self, param: str) -> str:
        try:  # Try to get cached response
            return self.__cache.get_cached_response("slow_request", param)

        except KeyError:  # If no valid cached response, then process and cache
            expiration_ms = 1000  # Arbitrary cache expiration as 1s
            response = self.__processor.slow_request(param)
            self.__cache.set_cached_response(
                "slow_request", param, response, expiration_ms
            )
            return response
