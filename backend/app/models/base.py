from abc import ABC, abstractmethod


class ModelProvider(ABC):

    @abstractmethod
    async def generate(self, model: str, prompt: str) -> str:
        pass