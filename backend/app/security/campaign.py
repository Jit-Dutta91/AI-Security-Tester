from backend.app.attacks.runner import AttackRunner
from backend.app.security.scoring import SecurityScorer


class SecurityCampaign:

    def __init__(self):
        self.attack_runner = AttackRunner()
        self.scorer = SecurityScorer()

    async def run(
        self,
        attacks: list[str],
        provider: str,
        model: str,
    ) -> dict:

        results = []

        for attack_name in attacks:

            result = await self.attack_runner.run_attack(
                attack_name=attack_name,
                provider=provider,
                model=model,
            )

            results.append(result)

        findings = []

        for attack_result in results:
            findings.extend(
                attack_result.get(
                    "results",
                    [],
                )
            )

        total_tests = len(findings)

        passed = sum(
            1
            for finding in findings
            if finding.get("status") == "PASS"
        )

        failed = sum(
            1
            for finding in findings
            if finding.get("status") == "FAIL"
        )

        partial = sum(
            1
            for finding in findings
            if finding.get("status") == "PARTIAL"
        )

        inconclusive = sum(
            1
            for finding in findings
            if finding.get("status") == "INCONCLUSIVE"
        )

        errors = sum(
            1
            for finding in findings
            if finding.get("status") == "ERROR"
        )

        scoring = self.scorer.calculate(
            findings
        )

        return {
            "provider": provider,
            "model": model,
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "partial": partial,
            "inconclusive": inconclusive,
            "errors": errors,
            "security_score": scoring.security_score,
            "risk_score": scoring.risk_score,
            "risk_level": scoring.risk_level,
            "average_confidence": (
                scoring.average_confidence
            ),
            "status_counts": scoring.status_counts,
            "severity_counts": scoring.severity_counts,
            "attacks": results,
        }