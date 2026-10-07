from backend.app.models.ollama import OllamaProvider


class ModelService:

    def __init__(self):
        self.providers = {
            "ollama": OllamaProvider(),
        }

    async def generate(
        self,
        provider: str,
        model: str,
        prompt: str,
    ) -> str:

        if provider not in self.providers:
            raise ValueError(
                f"Unsupported provider: {provider}"
            )

        selected_provider = self.providers[provider]

        return await selected_provider.generate(
            model=model,
            prompt=prompt,
        )