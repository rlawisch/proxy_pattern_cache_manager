import time
from abc import ABCMeta, abstractmethod


class IProcessor(metaclass=ABCMeta):
    @abstractmethod
    def slow_request(self, param: str) -> str:
        pass


class Processor(IProcessor):
    def slow_request(self, param: str) -> str:
        time.sleep(2)  # Arbitrary delay to simulate slowness

        return f"Response from request with param '{param}'"
