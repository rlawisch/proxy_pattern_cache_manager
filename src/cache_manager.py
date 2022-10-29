import time


class CacheObject:
    def __init__(
        self, request: str, param: str, response: str, expiration_ms: int
    ) -> None:
        self.__request = request
        self.__param = param
        self.__response = response
        self.__expiration = time.time_ns() + expiration_ms * 1_000_000

    def is_valid(self) -> bool:
        return self.__expiration >= time.time_ns()

    def get_request(self) -> str:
        return self.__request

    def get_param(self) -> str:
        return self.__param

    def get_response(self) -> str:
        return self.__response


class CacheManager:
    def __init__(self) -> None:
        self.__cache = {}

    def _make_key(self, request: str, param: str) -> str:
        return f"${request}_${param}"

    def get_cached_response(self, request: str, param: str) -> str:
        try:
            key = self._make_key(request, param)
            cache_object = self.__cache[key]
            if cache_object.is_valid():
                return cache_object.get_response()

            raise KeyError

        except KeyError:
            raise KeyError

    def set_cached_response(
        self, request: str, param: str, response: str, expiration_ms: int
    ):
        key = self._make_key(request, param)
        self.__cache[key] = CacheObject(request, param, response, expiration_ms)
