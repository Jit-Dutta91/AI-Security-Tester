# AI Security Tester — Multi-Model 70-Probe Comparison

## 1. Executive Summary

AI Security Tester was evaluated against four local Ollama models using the same 70-probe security baseline covering 14 security-testing categories.

The objective was to compare model behavior under a consistent security-testing methodology and identify differences in security-boundary resistance.

### Overall Results

| Model | Passed | Failed | Security Score | Risk Score | Risk Level |
|---|---:|---:|---:|---:|---|
| Qwen 3.5:4b | 70 | 0 | 100.00 | 0.00 | MINIMAL |
| Phi-3 | 58 | 12 | 68.24 | 31.76 | MEDIUM |
| Mistral | 53 | 17 | 57.61 | 42.39 | MEDIUM |
| Llama 3.2:1b | 47 | 23 | 49.47 | 50.53 | HIGH |

All four models completed the 70-probe campaign without execution errors.

Across the four models, the results demonstrate that different models can exhibit substantially different security-boundary behavior even when tested with the same security-testing suite.

---

## 2. Test Methodology

### Test Suite

- Total probes per model: **70**
- Security categories: **14**
- Probes per category: **5**
- Provider: **Ollama**
- Evaluation: **AI Security Tester heuristic evaluator**
- Execution environment: **Local Windows environment**
- Models: Qwen 3.5:4b, Phi-3, Mistral, Llama 3.2:1b

### Security Categories

1. Jailbreak
2. Prompt Injection
3. System Prompt Leakage
4. Safety
5. Robustness
6. Encoding / Obfuscation
7. Instruction Hierarchy
8. Context Manipulation
9. Sensitive Information Disclosure
10. Multi-Turn Consistency
11. Indirect Prompt Injection
12. RAG Security
13. Agent / Tool Authorization
14. Excessive Agency

---

## 3. Model Results

### Qwen 3.5:4b

- Total tests: 70
- Passed: 70
- Failed: 0
- Security score: **100.00**
- Risk score: **0.00**
- Risk level: **MINIMAL**
- Average confidence: **0.869**

Qwen 3.5:4b achieved a 100/100 result across the validated 70-probe baseline.

This result should be interpreted as the observed result of this security-testing baseline and not as a claim that the model is universally secure.

---

### Phi-3

- Total tests: 70
- Passed: 58
- Failed: 12
- Security score: **68.24**
- Risk score: **31.76**
- Risk level: **MEDIUM**
- Average confidence: **0.9286**

The primary observed weakness was system-prompt leakage, with 3 of 5 probes classified as failures.

Other observed failure areas included sensitive information disclosure, multi-turn consistency, encoding/obfuscation, instruction hierarchy, RAG security, agent/tool authorization, and excessive agency.

---

### Mistral

- Total tests: 70
- Passed: 53
- Failed: 17
- Security score: **57.61**
- Risk score: **42.39**
- Risk level: **MEDIUM**
- Average confidence: **0.9246**

The strongest observed weakness was context manipulation, with 3 of 5 probes classified as failures.

Additional failures occurred in jailbreak, safety, instruction hierarchy, multi-turn consistency, indirect prompt injection, system-prompt leakage, encoding/obfuscation, RAG security, and excessive agency.

---

### Llama 3.2:1b

- Total tests: 70
- Passed: 47
- Failed: 23
- Security score: **49.47**
- Risk score: **50.53**
- Risk level: **HIGH**
- Average confidence: **0.9147**

The strongest observed weaknesses were:

- Context manipulation: 5/5 failures
- Instruction hierarchy: 4/5 failures
- RAG security: 3/5 failures
- System prompt leakage: 2/5 failures
- Robustness: 2/5 failures
- Multi-turn consistency: 2/5 failures
- Agent/tool authorization: 2/5 failures

---

## 4. Category-Level Failure Matrix

The following matrix records the number of failed probes out of five in each category.

| Category | Qwen 3.5:4b | Phi-3 | Mistral | Llama 3.2:1b |
|---|---:|---:|---:|---:|
| Jailbreak | 0/5 | 0/5 | 2/5 | 0/5 |
| Prompt Injection | 0/5 | 0/5 | 0/5 | 0/5 |
| System Prompt Leakage | 0/5 | 3/5 | 1/5 | 2/5 |
| Safety | 0/5 | 0/5 | 2/5 | 0/5 |
| Robustness | 0/5 | 0/5 | 0/5 | 2/5 |
| Encoding / Obfuscation | 0/5 | 1/5 | 1/5 | 0/5 |
| Instruction Hierarchy | 0/5 | 1/5 | 2/5 | 4/5 |
| Context Manipulation | 0/5 | 0/5 | 3/5 | 5/5 |
| Sensitive Information Disclosure | 0/5 | 2/5 | 0/5 | 1/5 |
| Multi-Turn Consistency | 0/5 | 2/5 | 2/5 | 2/5 |
| Indirect Prompt Injection | 0/5 | 0/5 | 2/5 | 1/5 |
| RAG Security | 0/5 | 1/5 | 1/5 | 3/5 |
| Agent / Tool Authorization | 0/5 | 1/5 | 0/5 | 2/5 |
| Excessive Agency | 0/5 | 1/5 | 1/5 | 1/5 |

---

## 5. Key Observations

### Qwen 3.5:4b

Qwen produced the strongest result in this baseline, passing all 70 probes.

### Phi-3

Phi-3 showed a concentrated weakness around system-prompt leakage, with additional failures distributed across several advanced security categories.

### Mistral

Mistral showed its largest concentration of failures in context manipulation. It also demonstrated failures in jailbreak and safety-related probes.

### Llama 3.2:1b

Llama 3.2:1b produced the highest number of failures in this comparison. Context manipulation and instruction hierarchy were particularly weak areas.

### Overall Comparison

The results demonstrate that security behavior is not uniform across models. A model may perform well against one attack category while showing weaknesses in another.

This supports the use of category-specific security testing rather than relying on a single overall security measurement.

---

## 6. Important Interpretation

The security score represents the result produced by the current AI Security Tester evaluation framework.

It should be interpreted as:

> An observed security-testing score produced by the 70-probe baseline.

It should **not** be interpreted as:

- a universal security rating;
- proof that a model is completely secure;
- proof that a failed probe represents a confirmed real-world exploit;
- a replacement for comprehensive red-team testing.

Several categories currently use heuristic evaluation and simulated security scenarios rather than complete real-world environments.

For example, the current baseline does not constitute a complete:

- RAG poisoning environment;
- autonomous agent/tool execution environment;
- production multi-turn attack environment.

---

## 7. Evaluator Limitations

The current evaluator is deterministic and heuristic-based.

It evaluates model responses using security-boundary indicators, refusal patterns, security recognition, and category-specific compliance indicators.

This provides a reproducible baseline, but it can potentially produce:

- false positives;
- false negatives;
- failures where a response does not clearly demonstrate resistance;
- classification errors caused by ambiguous natural-language responses.

Therefore, important failures should be manually reviewed using the original model response before being described as confirmed vulnerabilities.

---

## 8. Reproducibility

The following result artifacts were preserved:

- 
eports/qwen3.5-4b-70-probe-baseline.json
- 
eports/phi3-70-probe-evaluator-v2.json
- 
eports/mistral-70-probe-evaluator-v2.json
- 
eports/llama3.2-1b-evaluator-v2.json

All four models used the same 70-probe campaign structure.

The model provider was:

ollama

The campaigns were executed through the AI Security Tester FastAPI backend.

---

## 9. Superseded Llama Result

An earlier Llama 3.2:1b result was generated using an earlier version of the evaluator:


eports/llama3.2-1b-70-probe-evaluator-v2.json

That artifact reported:

- 65 passed
- 5 failed
- Security score: 81.25
- Risk level: LOW

It was superseded after improvements were made to the evaluator to reduce false-positive classifications.

The authoritative Llama result for this comparison is:


eports/llama3.2-1b-evaluator-v2.json

which reports:

- 47 passed
- 23 failed
- Security score: **49.47**
- Risk level: **HIGH**

The superseded result must not be used for the final model comparison.

---

## 10. Demo Conclusion

The 70-probe comparison demonstrates the ability of AI Security Tester to evaluate multiple local models using a consistent security-testing methodology.

The observed results were:

**Qwen 3.5:4b → 100.00 / MINIMAL**

**Phi-3 → 68.24 / MEDIUM**

**Mistral → 57.61 / MEDIUM**

**Llama 3.2:1b → 49.47 / HIGH**

The most important demonstration point is not simply the ranking of the models, but the difference in their security failure profiles.

AI Security Tester can therefore be used to identify which security categories require additional investigation for a particular model.

---

## 11. Validation Status

| Validation | Status |
|---|---|
| Qwen 3.5:4b baseline | PASS |
| Phi-3 campaign | PASS |
| Mistral campaign | PASS |
| Llama 3.2:1b corrected campaign | PASS |
| Campaign execution errors | 0 |
| Partial results | 0 |
| Inconclusive results | 0 |
| Result artifacts preserved | PASS |

**Total probes executed across current comparison: 280**

**Total execution errors: 0**

---

*Generated for the AI Security Tester project. Results represent the observed behavior of the tested model versions under the project's current 70-probe heuristic baseline.*
