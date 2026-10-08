from backend.app.security.scoring import SecurityScorer


def test_all_pass_score_is_minimal():
    findings = [
        {
            "status": "PASS",
            "severity": "LOW",
            "confidence": 1.0,
        }
        for _ in range(70)
    ]

    result = SecurityScorer().calculate(findings)

    assert result.security_score == 100.0
    assert result.risk_score == 0.0
    assert result.risk_level == "MINIMAL"
    assert result.average_confidence == 1.0
    assert result.status_counts == {"PASS": 70}
    assert result.severity_counts == {"LOW": 70}
