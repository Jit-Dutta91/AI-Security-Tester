from datetime import datetime, timezone
from time import perf_counter

from backend.app.services.model_service import ModelService
from backend.app.attacks.registry import AttackRegistry


class AttackRunner:

    def __init__(self):
        self.model_service = ModelService()
        self.attack_registry = AttackRegistry()

    def _get_test_prefix(self, category: str) -> str:
        prefixes = {
            "jailbreak": "JAILBREAK",
            "prompt_injection": "PROMPT-INJECTION",
            "system_prompt_leakage": "LEAKAGE",
            "safety": "SAFETY",
        }

        return prefixes.get(
            category,
            category.upper().replace(" ", "-"),
        )

    def _get_severity(
        self,
        category: str,
        passed: bool,
    ) -> str:

        if passed:
            return "LOW"

        high_risk_categories = {
            "jailbreak",
            "prompt_injection",
            "system_prompt_leakage",
            "safety",
        }

        if category in high_risk_categories:
            return "HIGH"

        return "MEDIUM"

    def _get_status(self, passed: bool) -> str:
        if passed:
            return "PASS"

        return "FAIL"

    async def run_attack(
        self,
        attack_name: str,
        provider: str,
        model: str,
    ) -> dict:

        attack = self.attack_registry.get(
            attack_name
        )

        prompts = attack.get_prompts()

        results = []

        for index, prompt in enumerate(
            prompts,
            start=1,
        ):

            start_time = perf_counter()

            timestamp = datetime.now(
                timezone.utc
            ).isoformat()

            response = await self.model_service.generate(
                provider=provider,
                model=model,
                prompt=prompt,
            )

            duration_ms = round(
                (perf_counter() - start_time) * 1000,
                2,
            )

            evaluation = attack.evaluate(
                response
            )

            passed = (
                evaluation.get("passed") is True
            )

            status = self._get_status(
                passed
            )

            severity = self._get_severity(
                attack.category,
                passed,
            )

            confidence = evaluation.get(
                "confidence",
                0.0,
            )

            test_prefix = self._get_test_prefix(
                attack.category
            )

            test_id = (
                f"{test_prefix}-{index:03d}"
            )

            result = {
                "test_id": test_id,
                "test_number": index,
                "category": attack.category,
                "attack": attack.name,
                "status": status,
                "severity": severity,
                "confidence": confidence,
                "provider": provider,
                "model": model,
                "prompt": prompt,
                "response": response,
                "reason": evaluation.get(
                    "reason",
                    "",
                ),
                "timestamp": timestamp,
                "duration_ms": duration_ms,
                "evaluation": evaluation,
            }

            results.append(result)

        total_tests = len(results)

        passed = sum(
            1
            for result in results
            if result["status"] == "PASS"
        )

        failed = sum(
            1
            for result in results
            if result["status"] == "FAIL"
        )

        score = (
            (passed / total_tests) * 100
            if total_tests > 0
            else 0
        )

        return {
            "attack": attack.name,
            "category": attack.category,
            "provider": provider,
            "model": model,
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "score": score,
            "results": results,
        }