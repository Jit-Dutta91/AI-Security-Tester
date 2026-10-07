from backend.app.services.model_service import ModelService
from backend.app.security.baseline import BaselineInstructionTest
from backend.app.attacks.registry import AttackRegistry


class SecurityEngine:

    def __init__(self):
        self.model_service = ModelService()
        self.attack_registry = AttackRegistry()

        self.tests = {
            "baseline_instruction": BaselineInstructionTest(),
        }

    async def run_test(
        self,
        test_name: str,
        provider: str,
        model: str,
    ) -> dict:

        if test_name not in self.tests:
            raise ValueError(
                f"Unknown security test: {test_name}"
            )

        test = self.tests[test_name]

        prompt = test.generate_prompt()

        response = await self.model_service.generate(
            provider=provider,
            model=model,
            prompt=prompt,
        )

        evaluation = test.evaluate(response)

        return {
            "type": "security_test",
            "test": test.name,
            "category": test.category,
            "provider": provider,
            "model": model,
            "prompt": prompt,
            "response": response,
            "evaluation": evaluation,
        }

    async def run_attack(
        self,
        attack_name: str,
        provider: str,
        model: str,
    ) -> dict:

        attack = self.attack_registry.get(
            attack_name
        )

        prompt = attack.generate_prompt()

        response = await self.model_service.generate(
            provider=provider,
            model=model,
            prompt=prompt,
        )

        evaluation = attack.evaluate(response)

        return {
            "type": "attack",
            "attack": attack.name,
            "category": attack.category,
            "provider": provider,
            "model": model,
            "prompt": prompt,
            "response": response,
            "evaluation": evaluation,
        }