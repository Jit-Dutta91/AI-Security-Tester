# AI Security Tester

A modular AI/LLM security testing framework for evaluating local language models against common security risks such as jailbreaks, prompt injection, system-prompt leakage, instruction-hierarchy attacks, sensitive-information disclosure, indirect prompt injection, RAG security, and excessive agency.

The project currently provides a **FastAPI-based security testing backend**, an extensible attack registry, model-provider abstraction, deterministic security evaluation, scoring, baseline campaigns, automated tests, and reproducible multi-model evaluation reports.

> **Important:** This project is a security-testing and evaluation framework. A high score does **not** mean that a model is completely secure.

---

## Features

* Modular attack framework
* 14 security-testing categories
* 70-probe baseline suite
* 5 probes per category
* Ollama model-provider integration
* FastAPI REST API
* Provider abstraction for future model backends
* Automated response evaluation
* Security and risk scoring
* Severity and confidence tracking
* Campaign-based testing
* Multi-model comparison reports
* Automated regression tests
* UTF-8/BOM-clean source files
* Reproducible local testing
* Designed for future integration with n8n and a web-based GUI

---

# Security Test Categories

The current baseline contains **14 security categories** with **5 probes per category**, giving a total of **70 probes**.

| #  | Category                         | Baseline Probes |
| -- | -------------------------------- | --------------: |
| 1  | Jailbreak                        |               5 |
| 2  | Prompt Injection                 |               5 |
| 3  | System Prompt Leakage            |               5 |
| 4  | Safety                           |               5 |
| 5  | Robustness                       |               5 |
| 6  | Encoding / Obfuscation           |               5 |
| 7  | Instruction Hierarchy            |               5 |
| 8  | Context Manipulation             |               5 |
| 9  | Sensitive Information Disclosure |               5 |
| 10 | Multi-Turn Consistency           |               5 |
| 11 | Indirect Prompt Injection        |               5 |
| 12 | RAG Security                     |               5 |
| 13 | Agent / Tool Authorization       |               5 |
| 14 | Excessive Agency                 |               5 |
|    | **Total**                        |          **70** |

---

# Architecture

The current architecture is designed around separation between the API, attack engine, model providers, evaluation, and scoring layers.

```text
                         ┌──────────────────────┐
                         │     User / Client    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       FastAPI        │
                         │      REST API        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Security Campaign  │
                         │       Engine         │
                         └──────────┬───────────┘
                                    │
                         ┌──────────┴───────────┐
                         │                      │
                         ▼                      ▼
                ┌─────────────────┐    ┌─────────────────┐
                │ Attack Registry │    │ Model Provider  │
                │                 │    │   Abstraction   │
                └────────┬────────┘    └────────┬────────┘
                         │                      │
                         ▼                      ▼
                ┌─────────────────┐    ┌─────────────────┐
                │ 70 Security     │    │     Ollama      │
                │ Probes          │    │     Models      │
                └────────┬────────┘    └────────┬────────┘
                         │                      │
                         └──────────┬───────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   Target LLM Response │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Evaluator        │
                         │  Response Analysis   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Security Scorer    │
                         │ Risk / Score / Level │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Findings / Reports   │
                         └──────────────────────┘
```

---

# Project Structure

```text
AI-Security-Tester/
│
├── backend/
│   ├── __init__.py
│   │
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── attacks/
│       │   ├── base.py
│       │   ├── runner.py
│       │   ├── registry.py
│       │   │
│       │   ├── jailbreak/
│       │   ├── prompt_injection/
│       │   ├── leakage/
│       │   ├── safety/
│       │   └── ...
│       │
│       ├── models/
│       │   ├── base.py
│       │   └── ollama.py
│       │
│       ├── security/
│       │   ├── advanced_evaluator.py
│       │   ├── baseline.py
│       │   ├── campaign.py
│       │   ├── engine.py
│       │   ├── evaluator.py
│       │   ├── scoring.py
│       │   └── base.py
│       │
│       └── services/
│           └── model_service.py
│
├── reports/
│   ├── archive/
│   ├── qwen3.5-4b-70-probe-baseline.json
│   ├── phi3-70-probe-evaluator-v2.json
│   ├── mistral-70-probe-evaluator-v2.json
│   ├── llama3.2-1b-evaluator-v2.json
│   └── multi-model-70-probe-comparison.md
│
├── tests/
│   ├── test_imports.py
│   ├── test_registry.py
│   └── test_scoring.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── .venv/                  # local environment, not committed
```

---

# Requirements

## Runtime

* Windows, Linux, or macOS
* Python 3.12+
* FastAPI
* Uvicorn
* HTTPX
* Pydantic
* Ollama for local model testing

## Development / Testing

* pytest

The project separates runtime dependencies from development/test dependencies.

### Runtime dependencies

```powershell
pip install -r requirements.txt
```

### Development and test dependencies

```powershell
pip install -r requirements-dev.txt
```

`requirements-dev.txt` currently contains:

```text
-r requirements.txt
pytest==9.1.1
```

---

# Installation

## 1. Clone the repository

```powershell
git clone https://github.com/Jit-Dutta91/AI-Security-Tester.git
cd AI-Security-Tester
```

---

## 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install runtime dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Install development/test dependencies

```powershell
pip install -r requirements-dev.txt
```

---

# Ollama Setup

The current implementation uses Ollama as the local model provider.

Install Ollama and make sure its API is available at:

```text
http://localhost:11434
```

Verify the service:

```powershell
ollama list
```

Example models used during project validation:

```text
qwen3.5:4b
phi3:latest
mistral:latest
llama3.2:1b
```

Pull a model if required:

```powershell
ollama pull qwen3.5:4b
```

Verify the model:

```powershell
ollama list
```

---

# Validate the Python Environment

Check Python:

```powershell
python --version
```

Check dependency health:

```powershell
python -m pip check
```

Expected:

```text
No broken requirements found.
```

---

# Run the Test Suite

The repository contains automated tests for the core framework.

Run:

```powershell
python -m pytest .\tests -v
```

Expected result for the current test suite:

```text
4 passed
```

The current tests validate:

* Backend imports
* 14 registered attack categories
* 70 total baseline probes
* Security scoring behavior

Example:

```text
tests/test_imports.py::test_backend_imports PASSED
tests/test_registry.py::test_attack_registry_contains_14_attacks PASSED
tests/test_registry.py::test_attack_registry_contains_70_probes PASSED
tests/test_scoring.py::test_all_pass_score_is_minimal PASSED

4 passed
```

---

# Start the FastAPI Server

From the repository root:

```powershell
uvicorn backend.app.main:app --reload
```

The API should start at:

```text
http://127.0.0.1:8000
```

---

# Health Check

Verify that the backend is running:

```powershell
python -c "import urllib.request, json; r=urllib.request.urlopen('http://127.0.0.1:8000/health'); print(r.status); print(json.loads(r.read()))"
```

Expected:

```text
200
{'status': 'ok', 'service': 'AI Security Tester', 'version': '0.1.0'}
```

---

# API Endpoints

## Health

```text
GET /health
```

Example:

```powershell
Invoke-RestMethod `
    -Uri "http://127.0.0.1:8000/health" `
    -Method Get
```

Expected:

```json
{
  "status": "ok",
  "service": "AI Security Tester",
  "version": "0.1.0"
}
```

---

# Model Integration Test

The backend exposes a model testing endpoint for validating provider connectivity.

```text
POST /models/test
```

Example PowerShell request:

```powershell
$body = @{
    provider = "ollama"
    model    = "qwen3.5:4b"
    prompt   = "Reply with exactly: API-TEST-OK"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:8000/models/test" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

Expected response:

```text
provider model      prompt                          response
-------- -----      ------                          --------
ollama   qwen3.5:4b Reply with exactly: API-TEST-OK API-TEST-OK
```

This confirms:

```text
FastAPI
   ↓
Model Service
   ↓
Ollama Provider
   ↓
Ollama
   ↓
Target Model
```

---

# Security Campaigns

The main security campaign endpoint is:

```text
POST /security/campaign
```

A campaign can specify:

* attack categories
* model provider
* target model

Example request:

```json
{
  "attacks": [
    "basic_jailbreak",
    "basic_prompt_injection",
    "basic_system_prompt_leakage",
    "basic_safety",
    "basic_robustness",
    "basic_encoding_obfuscation",
    "basic_instruction_hierarchy",
    "basic_context_manipulation",
    "basic_sensitive_information_disclosure",
    "basic_multi_turn_consistency",
    "basic_indirect_prompt_injection",
    "basic_rag_security",
    "basic_agent_tool_authorization",
    "basic_excessive_agency"
  ],
  "provider": "ollama",
  "model": "qwen3.5:4b"
}
```

The complete baseline therefore contains:

```text
14 categories × 5 probes = 70 probes
```

---

# Attack Registry

The attack registry provides a centralized mechanism for discovering and executing registered attacks.

The current registry contains:

```text
basic_jailbreak
basic_prompt_injection
basic_system_prompt_leakage
basic_safety
basic_robustness
basic_encoding_obfuscation
basic_instruction_hierarchy
basic_context_manipulation
basic_sensitive_information_disclosure
basic_multi_turn_consistency
basic_indirect_prompt_injection
basic_rag_security
basic_agent_tool_authorization
basic_excessive_agency
```

The registry is designed so that additional attack modules can be added without rewriting the campaign engine.

---

# Model Provider Architecture

The project uses a provider abstraction rather than coupling the security engine directly to a specific model platform.

Conceptually:

```text
ModelProvider
     │
     ├── OllamaProvider
     │
     ├── FutureProvider
     │
     └── FutureProvider
```

The provider interface allows future integrations with additional model backends while keeping the security-testing layer independent.

Current provider:

```text
Ollama
```

Future providers can be implemented using the same abstraction.

---

# Evaluation Engine

The evaluator analyzes model responses to determine whether a security probe appears to have been resisted or complied with.

The evaluation logic considers indicators such as:

* explicit refusal
* security recognition
* authorization requirements
* unsafe commitment
* instruction bypass
* disclosure behavior
* category-specific compliance indicators

The evaluator is intentionally deterministic for the current baseline.

This makes results easier to reproduce than relying entirely on a second LLM to judge the output.

---

# Scoring

The security scorer aggregates individual findings into a campaign-level result.

The result includes:

* total tests
* passed tests
* failed tests
* partial tests
* inconclusive tests
* errors
* security score
* risk score
* risk level
* average confidence
* severity counts
* status counts

Example conceptual output:

```text
Total Tests:       70
Passed:            70
Failed:             0
Security Score:  100.00
Risk Score:        0.00
Risk Level:    MINIMAL
```

---

# Score Interpretation

The score represents performance against **this project's implemented test suite**.

It should not be interpreted as a universal security guarantee.

For example:

```text
100/100
```

means:

> The model passed all probes in the current 70-probe baseline according to the project's current evaluator.

It does **not** mean:

> The model is completely secure.

The test suite has limited coverage and deterministic evaluation logic, so results should be treated as an evaluation signal rather than proof of complete security.

---

# Multi-Model Evaluation

The baseline was executed against four local models.

All four models completed the full 70-probe suite.

Total probes executed:

```text
4 models × 70 probes = 280 probes
```

Total errors:

```text
0
```

---

## Qwen 3.5:4b

```text
Total:             70
Passed:            70
Failed:             0
Partial:            0
Inconclusive:       0
Errors:             0
Security Score: 100.00
Risk Score:       0.00
Risk Level:   MINIMAL
```

Result:

```text
70/70 probes passed
```

Report:

```text
reports/qwen3.5-4b-70-probe-baseline.json
```

---

## Phi-3

```text
Total:             70
Passed:            58
Failed:            12
Security Score: 68.24
Risk Score:      31.76
Risk Level:      MEDIUM
```

Notable failure areas included:

* System prompt leakage
* Encoding / obfuscation
* Instruction hierarchy
* Sensitive information disclosure
* Multi-turn consistency
* RAG security
* Agent / tool authorization
* Excessive agency

Report:

```text
reports/phi3-70-probe-evaluator-v2.json
```

---

## Mistral

```text
Total:             70
Passed:            53
Failed:            17
Security Score: 57.61
Risk Score:      42.39
Risk Level:      MEDIUM
```

Notable failure areas included:

* Jailbreak
* System prompt leakage
* Safety
* Encoding / obfuscation
* Instruction hierarchy
* Context manipulation
* Multi-turn consistency
* Indirect prompt injection
* RAG security
* Excessive agency

Report:

```text
reports/mistral-70-probe-evaluator-v2.json
```

---

## Llama 3.2:1b

```text
Total:             70
Passed:            47
Failed:            23
Security Score: 49.47
Risk Score:      50.53
Risk Level:        HIGH
```

Notable failure areas included:

* System prompt leakage
* Robustness
* Instruction hierarchy
* Context manipulation
* Sensitive information disclosure
* Multi-turn consistency
* Indirect prompt injection
* RAG security
* Agent / tool authorization
* Excessive agency

Report:

```text
reports/llama3.2-1b-evaluator-v2.json
```

---

# Multi-Model Comparison

| Category                         | Qwen 3.5:4b | Phi-3 | Mistral | Llama 3.2:1b |
| -------------------------------- | ----------: | ----: | ------: | -----------: |
| Jailbreak                        |         0/5 |   0/5 |     2/5 |          0/5 |
| Prompt Injection                 |         0/5 |   0/5 |     0/5 |          0/5 |
| System Prompt Leakage            |         0/5 |   3/5 |     1/5 |          2/5 |
| Safety                           |         0/5 |   0/5 |     2/5 |          0/5 |
| Robustness                       |         0/5 |   0/5 |     0/5 |          2/5 |
| Encoding / Obfuscation           |         0/5 |   1/5 |     1/5 |          0/5 |
| Instruction Hierarchy            |         0/5 |   1/5 |     2/5 |          4/5 |
| Context Manipulation             |         0/5 |   0/5 |     3/5 |          5/5 |
| Sensitive Information Disclosure |         0/5 |   2/5 |     0/5 |          1/5 |
| Multi-Turn Consistency           |         0/5 |   2/5 |     2/5 |          2/5 |
| Indirect Prompt Injection        |         0/5 |   0/5 |     2/5 |          1/5 |
| RAG Security                     |         0/5 |   1/5 |     1/5 |          3/5 |
| Agent / Tool Authorization       |         0/5 |   1/5 |     0/5 |          2/5 |
| Excessive Agency                 |         0/5 |   1/5 |     1/5 |          1/5 |

Detailed comparison:

```text
reports/multi-model-70-probe-comparison.md
```

---

# Reproducibility

A primary goal of the project is to make local model security evaluations reproducible.

Recommended workflow:

```powershell
# Activate environment
.\.venv\Scripts\Activate.ps1

# Verify dependencies
python -m pip check

# Run automated tests
python -m pytest .\tests -v

# Start API
uvicorn backend.app.main:app --reload
```

Then verify:

```text
/health
```

and:

```text
/models/test
```

before running a complete campaign.

---

# Windows Encoding / BOM Considerations

During development on Windows, PowerShell file-writing commands can create a UTF-8 Byte Order Mark (BOM), depending on the command and PowerShell version.

A BOM at the beginning of a Python source file can cause problems with certain tooling, file discovery, or source parsing.

For example, this command can introduce encoding differences depending on the environment:

```powershell
Set-Content -Encoding utf8
```

The project source files should therefore be maintained as:

```text
UTF-8 without BOM
```

To normalize a Python file:

```powershell
python -c "from pathlib import Path; p=Path('path/to/file.py'); p.write_text(p.read_text(encoding='utf-8-sig'), encoding='utf-8')"
```

To normalize all Python files under `backend`:

```powershell
python -c "from pathlib import Path; root=Path('backend'); [p.write_text(p.read_text(encoding='utf-8-sig'), encoding='utf-8', newline='') for p in root.rglob('*.py')]"
```

To check a file for a UTF-8 BOM:

```powershell
python -c "from pathlib import Path; p=Path('README.md'); b=p.read_bytes(); print('BOM:', b.startswith(b'\xef\xbb\xbf')); p.read_text(encoding='utf-8'); print('UTF-8: OK')"
```

This repository is maintained with UTF-8/BOM-clean source and documentation files.

---

# Development Validation

The current release has been validated with:

### Dependency validation

```text
python -m pip check
```

Result:

```text
No broken requirements found.
```

### Automated tests

```text
python -m pytest .\tests -v
```

Result:

```text
4 passed
```

### Attack registry validation

```text
14 registered attack categories
70 total probes
5 probes per category
```

### Backend import validation

```text
backend.app.main
```

Result:

```text
MAIN IMPORT: OK
```

### FastAPI health validation

```text
HTTP 200
```

### Ollama integration validation

```text
FastAPI → Ollama → qwen3.5:4b
```

Result:

```text
API-TEST-OK
```

### Multi-model baseline validation

```text
4 models
70 probes per model
280 total probes
0 execution errors
```

---

# Current Scope and Limitations

The project is currently a **baseline LLM security-testing framework**, not a complete enterprise red-team platform.

Several categories require more sophisticated environments for full validation.

## RAG Security

The current RAG tests evaluate security behavior conceptually.

They do not yet provide a complete production RAG environment containing:

* document ingestion
* vector database
* retrieval pipeline
* permission-aware document access
* poisoned documents
* retrieval isolation
* citation validation

A future implementation should connect the evaluator to an actual RAG pipeline.

---

## Agent / Tool Authorization

The current tests evaluate model responses related to tool authorization.

They do not currently execute arbitrary real-world tools against production systems.

A full agent-security implementation should test:

* tool allowlists
* authentication
* authorization
* privilege boundaries
* parameter validation
* tool output handling
* approval workflows
* dangerous-action confirmation

---

## Excessive Agency

The current excessive-agency category focuses primarily on model behavior.

A complete implementation should additionally evaluate an actual agent with:

* filesystem access
* shell execution
* network access
* APIs
* credentials
* tool permissions
* action approval controls

---

## Multi-Turn Consistency

The current baseline contains probes for multi-turn behavior, but the framework should eventually model complete conversation histories rather than treating every probe as an isolated request.

Future implementations should test:

* memory manipulation
* instruction persistence
* role transitions
* delayed jailbreaks
* context poisoning
* cross-turn privilege escalation

---

## Evaluator Limitations

The evaluator currently uses deterministic heuristics and category-specific indicators.

This provides:

* reproducibility
* transparency
* predictable scoring
* low infrastructure requirements

However, heuristic evaluation can produce:

* false positives
* false negatives
* context-insensitive classifications
* incomplete interpretation of nuanced responses

Future versions may support multiple evaluation strategies, including model-assisted judging and structured semantic analysis.

---

# Security Considerations

Do not use this project against systems or models that you do not own or have explicit permission to test.

Security testing can intentionally generate:

* jailbreak attempts
* malicious instructions
* sensitive-information requests
* prompt-injection payloads
* authorization bypass attempts
* potentially unsafe model outputs

Use isolated test environments whenever possible.

Do not place:

* API keys
* passwords
* access tokens
* private credentials
* production secrets

inside source files, prompts, reports, or Git commits.

Use environment variables or an appropriate secret-management mechanism for sensitive configuration.

---

# Git and Release Hygiene

The repository intentionally excludes local/generated artifacts such as:

```text
.venv/
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.env
logs
```

The `.gitignore` file should prevent these files from being committed.

Before creating a release commit, verify:

```powershell
git status
```

and ensure that unexpected generated files are not present.

A clean working tree should eventually show:

```text
nothing to commit, working tree clean
```

---

# Future Development

Planned development areas include:

### Web GUI

A web interface for:

* model selection
* campaign configuration
* attack selection
* live execution status
* findings
* scoring
* reports
* model comparison

---

### n8n Integration

n8n can eventually provide workflow orchestration for:

```text
Campaign
   ↓
Model Testing
   ↓
Security Evaluation
   ↓
Scoring
   ↓
Report Generation
   ↓
Notification / Storage
```

The security engine remains separated from workflow orchestration so that the core testing functionality can operate independently.

---

### Additional Model Providers

Future provider adapters may support additional local or remote model backends while preserving the same `ModelProvider` interface.

---

### Advanced Attack Generation

Future releases can introduce:

* adaptive attacks
* mutation-based prompts
* automated payload generation
* multilingual attacks
* encoding transformations
* multi-turn attack chains
* context poisoning
* agent attack chains
* RAG poisoning
* tool abuse scenarios

---

### Improved Evaluation

Future evaluation capabilities may include:

* structured model judging
* ensemble evaluators
* semantic similarity analysis
* attack-specific scoring
* confidence calibration
* human-review workflows
* evidence extraction

---

# Project Status

Current implementation status:

| Component                  | Status   |
| -------------------------- | -------- |
| FastAPI backend            | Complete |
| Ollama provider            | Complete |
| Provider abstraction       | Complete |
| Attack registry            | Complete |
| 14 security categories     | Complete |
| 70-probe baseline          | Complete |
| Deterministic evaluator    | Complete |
| Security scoring           | Complete |
| Automated regression tests | Complete |
| Multi-model evaluation     | Complete |
| Comparison report          | Complete |
| Web GUI                    | Future   |
| n8n orchestration          | Future   |
| Full RAG environment       | Future   |
| Full agent/tool sandbox    | Future   |
| Advanced adaptive attacks  | Future   |

---

# Validation Summary

The current implementation has been validated locally with:

```text
Python:              3.12.0
FastAPI:             0.142.2
Pytest:              9.1.1
Registered attacks:  14
Baseline probes:     70
Models evaluated:    4
Total probes:        280
Execution errors:    0
Automated tests:     4 passed
```

The baseline model results were:

| Model        | Passed | Failed | Security Score | Risk Level |
| ------------ | -----: | -----: | -------------: | ---------- |
| Qwen 3.5:4b  |     70 |      0 |         100.00 | MINIMAL    |
| Phi-3        |     58 |     12 |          68.24 | MEDIUM     |
| Mistral      |     53 |     17 |          57.61 | MEDIUM     |
| Llama 3.2:1b |     47 |     23 |          49.47 | HIGH       |

These scores describe performance against the project's **current 70-probe baseline only**.

---

# Author

**Jit Dutta**

GitHub:

`Jit-Dutta91`

Repository:

`https://github.com/Jit-Dutta91/AI-Security-Tester`

---

# License

License information should be added here once the project license has been finalized.

---

## Disclaimer

This project is intended for authorized security research, defensive testing, education, and evaluation of AI systems.

The results produced by this framework should not be interpreted as proof that a model or AI application is secure. Security assessment should consider the complete application, model configuration, system prompts, tools, data sources, authentication, authorization, infrastructure, and deployment environment.
