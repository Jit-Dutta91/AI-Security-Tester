from abc import ABC, abstractmethod


class Attack(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def generate_prompt(self) -> str:
        pass

    @abstractmethod
    def evaluate(self, response: str) -> dict:
        pass