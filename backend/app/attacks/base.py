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
    def get_prompts(self) -> list[str]:
        pass

    def generate_prompt(self) -> str:
        prompts = self.get_prompts()

        if not prompts:
            raise ValueError(
                f"Attack '{self.name}' does not contain any prompts."
            )

        return prompts[0]

    @abstractmethod
    def evaluate(self, response: str) -> dict:
        pass