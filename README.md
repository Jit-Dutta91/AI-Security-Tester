\# AI Security Tester



AI Security Tester is a modular security testing platform for evaluating Large Language Models (LLMs) against a collection of security-oriented test categories.



The project provides a FastAPI backend, model-provider abstraction, modular attack framework, security evaluators, and campaign-based testing.



The same security test suite can be used to evaluate different AI models and compare their security behavior.



> \*\*Important:\*\* A passing score means that the model passed the specific tests implemented in this test suite. It does \*\*not\*\* guarantee that the model is universally secure or resistant to all possible attacks.



\---



\## Features



\* FastAPI REST API

\* Swagger/OpenAPI interface

\* Local AI model testing

\* Model provider abstraction

\* Modular attack framework

\* Attack registry

\* Individual security-test execution

\* Multi-attack security campaigns

\* Deterministic baseline evaluation

\* Security score

\* Risk score

\* Risk-level classification

\* Per-test results

\* Severity classification

\* Confidence values

\* Extensible attack categories

\* Support architecture for additional AI providers



\---



\# Architecture



```text
                      AI Security Tester

                              │
                              ▼
                      ┌─────────────────┐

                      │     FastAPI     │
                      │   REST Backend  │

                      └────────┬────────┘

                               │

                               ▼

                      ┌─────────────────┐

                      │ Security Engine │

                      └────────┬────────┘

                               │

                               ▼

                      ┌─────────────────┐

                      │Security Campaign│

                      └────────┬────────┘

                               │

                               ▼

                      ┌─────────────────┐

                      │ Attack Registry │

                      └────────┬────────┘

                               │

                               ▼

                      ┌─────────────────┐

                      │  Attack Runner  │

                      └────────┬────────┘

                               │

                               ▼

                      ┌─────────────────┐

                      │  Model Service  │

                      │    Provider     │

                      │   Abstraction   │

                      └────────┬────────┘

                               │

                 ┌─────────────┴─────────────┐

                 │                           │

                 ▼                           ▼

          Local AI Model              Non-Local AI

             Ollama                  API Provider

                 │                           │

                 └─────────────┬─────────────┘

                               │

                               ▼
                      ┌─────────────────┐

                      │    Evaluator    │

                      └────────┬────────┘

                               │

                               ▼

                      ┌─────────────────┐

                      │ Results / Score │

                      │ / Risk Analysis │

                      └─────────────────┘




\---



\# Project Structure



```text

AI-Security-Tester/

│

├── attacks/

│   ├── jailbreak/

│   ├── leakage/

│   ├── prompt\_injection/

│   ├── robustness/

│   └── safety/

│

├── backend/

│   └── app/

│       ├── attacks/

│       ├── models/

│       ├── security/

│       ├── services/

│       └── main.py

│

├── evaluations/

├── frontend/

├── reports/

├── tests/

├── workflows/

│

├── .gitignore

├── requirements.txt

└── README.md

```



\---



\# Requirements



\## Operating System



The currently validated environment is:



\* Windows 10/11

\* Python 3.12

\* Git

\* Ollama for local AI testing



The backend is implemented using Python and FastAPI.



\---



\# Installation



\## 1. Clone the Repository



```powershell

git clone <YOUR-GITHUB-REPOSITORY-URL>

cd AI-Security-Tester

```



\---



\## 2. Create a Virtual Environment



```powershell

python -m venv .venv

```



Activate it:



```powershell

.venv\\Scripts\\Activate.ps1

```



If PowerShell blocks script execution:



```powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

```



Then:



```powershell

.venv\\Scripts\\Activate.ps1

```



\---



\## 3. Install Dependencies



Upgrade pip:



```powershell

python -m pip install --upgrade pip

```



Install project dependencies:



```powershell

pip install -r requirements.txt

```



Verify:



```powershell

python -m pip check

```



Expected:



```text

No broken requirements found.

```



\---



\# Local AI Testing



The currently validated local configuration uses:



```text

Ollama

   ↓

qwen3.5:4b

   ↓

AI Security Tester

```



\---



\## 1. Install Ollama



Install Ollama for Windows.



Verify:



```powershell

ollama --version

```



\---



\## 2. Download the Model



```powershell

ollama pull qwen3.5:4b

```



Verify:



```powershell

ollama list

```



The model should appear as:



```text

qwen3.5:4b

```



\---



\# Test Ollama Directly



Before running AI Security Tester, verify that Ollama itself is working.



Run:



```powershell

Invoke-RestMethod `  -Uri "http://localhost:11434/api/generate" `

   -Method Post `

   -ContentType "application/json" `

   -Body '{"model":"qwen3.5:4b","prompt":"Reply with exactly: OLLAMA-TEST-OK","stream":false}'

```



The response should contain:



```text

OLLAMA-TEST-OK

```



If this fails, fix the Ollama/model configuration before continuing.



\---



\# Start AI Security Tester



From the project root:



```powershell

uvicorn backend.app.main:app --reload

```



The backend will run at:



```text

http://127.0.0.1:8000

```



Swagger/OpenAPI:



```text

http://127.0.0.1:8000/docs

```



\---



\# Verify the Backend



Open:



```text

http://127.0.0.1:8000/health

```



Expected response:



```json

{

 "status": "ok",

 "service": "AI Security Tester",

 "version": "0.1.0"

}

```



\---



\# Test the AI Model Through the API



Open Swagger:



```text

http://127.0.0.1:8000/docs

```



Find:



```text

POST /models/test

```



Select:



```text

Try it out

```



Use:



```json

{

 "provider": "ollama",

 "model": "qwen3.5:4b",

 "prompt": "Reply with exactly: API-TEST-OK"

}

```



The response should contain:



```text

API-TEST-OK

```



This verifies:



```text

FastAPI

  ↓

ModelService

  ↓

OllamaProvider

  ↓

Ollama

  ↓

qwen3.5:4b

```



\---



\# Run a Single Security Test



Use:



```text

POST /security/test

```



Example:



```json

{

 "test": "baseline",

 "provider": "ollama",

 "model": "qwen3.5:4b"

}

```



This verifies that the security engine can communicate with the selected model and evaluate the response.



\---



\# Run a Single Attack



Use:



```text

POST /security/attack

```



Example:



```json

{

 "attack": "basic\_jailbreak",

 "provider": "ollama",

 "model": "qwen3.5:4b"

}

```



The response contains information about the executed security probes and their evaluations.



\---



\# Run the Complete Security Campaign



The current baseline contains:



```text

14 attack categories

×

5 probes per category

=

70 security tests

```



Use:



```text

POST /security/campaign

```



Request:



```json

{

 "attacks": \[

   "basic\_jailbreak",

   "basic\_prompt\_injection",

   "basic\_system\_prompt\_leakage",

   "basic\_safety",

   "basic\_robustness",

   "basic\_encoding\_obfuscation",

   "basic\_instruction\_hierarchy",

   "basic\_context\_manipulation",

   "basic\_sensitive\_information\_disclosure",

   "basic\_multi\_turn\_consistency",

   "basic\_indirect\_prompt\_injection",

   "basic\_rag\_security",

   "basic\_agent\_tool\_authorization",

   "basic\_excessive\_agency"

 ],

 "provider": "ollama",

 "model": "qwen3.5:4b"

}

```



Execute the request using Swagger's:



```text

Try it out

→ Execute

```



\---



\# Current Attack Categories



| Category                         | Attack ID                                |

| -------------------------------- | ---------------------------------------- |

| Jailbreak                        | `basic\_jailbreak`                        |

| Prompt Injection                 | `basic\_prompt\_injection`                 |

| System Prompt Leakage            | `basic\_system\_prompt\_leakage`            |

| Safety                           | `basic\_safety`                           |

| Robustness                       | `basic\_robustness`                       |

| Encoding / Obfuscation           | `basic\_encoding\_obfuscation`             |

| Instruction Hierarchy            | `basic\_instruction\_hierarchy`            |

| Context Manipulation             | `basic\_context\_manipulation`             |

| Sensitive Information Disclosure | `basic\_sensitive\_information\_disclosure` |

| Multi-turn Consistency           | `basic\_multi\_turn\_consistency`           |

| Indirect Prompt Injection        | `basic\_indirect\_prompt\_injection`        |

| RAG Security                     | `basic\_rag\_security`                     |

| Agent / Tool Authorization       | `basic\_agent\_tool\_authorization`         |

| Excessive Agency                 | `basic\_excessive\_agency`                 |



\---



\# Understanding Campaign Results



A campaign result contains fields such as:



```text

total\_tests

passed

failed

partial

inconclusive

errors

security\_score

risk\_score

risk\_level

average\_confidence

status\_counts

severity\_counts

results

```



For example:



```text

Total tests: 70

Passed: 70

Failed: 0



Security score: 100

Risk score: 0

Risk level: MINIMAL

```



This means the model passed all tests in the implemented baseline suite.



It does \*\*not\*\* mean the model is universally secure.



\---



\# Validated Local Test Result



The current validated configuration is:



```text

Provider: Ollama

Model: qwen3.5:4b



Total tests:       70

Passed:            70

Failed:             0

Partial:            0

Inconclusive:       0

Errors:             0



Security score:   100/100

Risk score:         0

Risk level:       MINIMAL



Attack categories: 14

Probes/category:    5

```



Each of the 14 categories achieved:



```text

5/5 PASS

``

```



