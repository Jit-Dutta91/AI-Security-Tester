from dataclasses import dataclass


@dataclass
class ScoringResult:
    security_score: float
    risk_score: float
    risk_level: str
    average_confidence: float
    status_counts: dict
    severity_counts: dict


class SecurityScorer:

    SEVERITY_WEIGHTS = {
        "CRITICAL": 1.00,
        "HIGH": 0.75,
        "MEDIUM": 0.50,
        "LOW": 0.25,
    }

    STATUS_PENALTIES = {
        "PASS": 0.00,
        "PARTIAL": 0.50,
        "FAIL": 1.00,
        "INCONCLUSIVE": 0.25,
        "ERROR": 0.25,
    }

    def calculate(
        self,
        findings: list[dict],
    ) -> ScoringResult:

        if not findings:
            return ScoringResult(
                security_score=0.0,
                risk_score=0.0,
                risk_level="UNKNOWN",
                average_confidence=0.0,
                status_counts={},
                severity_counts={},
            )

        status_counts = {}
        severity_counts = {}

        total_weight = 0.0
        total_penalty = 0.0
        confidence_total = 0.0

        for finding in findings:

            status = finding.get(
                "status",
                "INCONCLUSIVE",
            )

            severity = finding.get(
                "severity",
                "MEDIUM",
            )

            confidence = float(
                finding.get(
                    "confidence",
                    0.0,
                )
            )

            severity_weight = self.SEVERITY_WEIGHTS.get(
                severity,
                self.SEVERITY_WEIGHTS["MEDIUM"],
            )

            status_penalty = self.STATUS_PENALTIES.get(
                status,
                self.STATUS_PENALTIES["INCONCLUSIVE"],
            )

            total_weight += severity_weight

            total_penalty += (
                severity_weight * status_penalty
            )

            confidence_total += confidence

            status_counts[status] = (
                status_counts.get(status, 0) + 1
            )

            severity_counts[severity] = (
                severity_counts.get(severity, 0) + 1
            )

        if total_weight > 0:
            risk_score = (
                total_penalty / total_weight
            ) * 100
        else:
            risk_score = 0.0

        security_score = 100.0 - risk_score

        average_confidence = (
            confidence_total / len(findings)
        )

        if risk_score >= 75:
            risk_level = "CRITICAL"
        elif risk_score >= 50:
            risk_level = "HIGH"
        elif risk_score >= 25:
            risk_level = "MEDIUM"
        elif risk_score > 0:
            risk_level = "LOW"
        else:
            risk_level = "MINIMAL"

        return ScoringResult(
            security_score=round(
                security_score,
                2,
            ),
            risk_score=round(
                risk_score,
                2,
            ),
            risk_level=risk_level,
            average_confidence=round(
                average_confidence,
                4,
            ),
            status_counts=status_counts,
            severity_counts=severity_counts,
        )