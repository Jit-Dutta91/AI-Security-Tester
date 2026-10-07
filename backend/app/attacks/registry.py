from backend.app.attacks.jailbreak.basic import BasicJailbreakAttack
from backend.app.attacks.prompt_injection.basic import BasicPromptInjectionAttack
from backend.app.attacks.leakage.basic import BasicLeakageAttack
from backend.app.attacks.safety.basic import BasicSafetyAttack

from backend.app.attacks.robustness.basic import RobustnessAttack
from backend.app.attacks.encoding_obfuscation.basic import EncodingObfuscationAttack
from backend.app.attacks.instruction_hierarchy.basic import InstructionHierarchyAttack
from backend.app.attacks.context_manipulation.basic import ContextManipulationAttack
from backend.app.attacks.sensitive_information_disclosure.basic import SensitiveInformationDisclosureAttack
from backend.app.attacks.multi_turn_consistency.basic import MultiTurnConsistencyAttack
from backend.app.attacks.indirect_prompt_injection.basic import IndirectPromptInjectionAttack
from backend.app.attacks.rag_security.basic import RagSecurityAttack
from backend.app.attacks.agent_tool_authorization.basic import AgentToolAuthorizationAttack
from backend.app.attacks.excessive_agency.basic import ExcessiveAgencyAttack


class AttackRegistry:

    def __init__(self):
        self.attacks = {}

        for attack in [
            BasicJailbreakAttack(),
            BasicPromptInjectionAttack(),
            BasicLeakageAttack(),
            BasicSafetyAttack(),
            RobustnessAttack(),
            EncodingObfuscationAttack(),
            InstructionHierarchyAttack(),
            ContextManipulationAttack(),
            SensitiveInformationDisclosureAttack(),
            MultiTurnConsistencyAttack(),
            IndirectPromptInjectionAttack(),
            RagSecurityAttack(),
            AgentToolAuthorizationAttack(),
            ExcessiveAgencyAttack(),
        ]:
            self.register(attack)

    def register(self, attack):
        self.attacks[attack.name] = attack

    def get(self, name: str):
        if name not in self.attacks:
            raise ValueError(f"Unknown attack: {name}")
        return self.attacks[name]

    def list_attacks(self):
        return list(self.attacks.keys())
