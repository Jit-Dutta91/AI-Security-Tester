from backend.app.attacks.registry import AttackRegistry


def test_attack_registry_contains_14_attacks():
    registry = AttackRegistry()

    attacks = registry.list_attacks()

    assert len(attacks) == 14


def test_attack_registry_contains_70_probes():
    registry = AttackRegistry()

    total_probes = sum(
        len(registry.get(name).get_prompts())
        for name in registry.list_attacks()
    )

    assert total_probes == 70
