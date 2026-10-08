from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.app.services.model_service import ModelService
from backend.app.security.engine import SecurityEngine
from backend.app.security.campaign import SecurityCampaign


app = FastAPI(
    title="AI Security Tester",
    description="AI model security testing platform",
    version="0.1.0",
)


model_service = ModelService()
security_engine = SecurityEngine()
security_campaign = SecurityCampaign()


# -----------------------------
# Request Models
# -----------------------------

class SecurityTestRequest(BaseModel):
    test: str
    provider: str
    model: str


class ModelTestRequest(BaseModel):
    provider: str
    model: str
    prompt: str


class AttackRequest(BaseModel):
    attack: str
    provider: str
    model: str


class CampaignRequest(BaseModel):
    attacks: list[str]
    provider: str
    model: str


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "service": "AI Security Tester",
        "version": "0.1.0",
    }


# -----------------------------
# Direct Model Test
# -----------------------------

@app.post("/models/test")
async def test_model(request: ModelTestRequest):

    try:

        response = await model_service.generate(
            provider=request.provider,
            model=request.model,
            prompt=request.prompt,
        )

        return {
            "provider": request.provider,
            "model": request.model,
            "prompt": request.prompt,
            "response": response,
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail=f"Model provider error: {error}",
        )


# -----------------------------
# Security Test
# -----------------------------

@app.post("/security/test")
async def run_security_test(
    request: SecurityTestRequest
):

    try:

        result = await security_engine.run_test(
            test_name=request.test,
            provider=request.provider,
            model=request.model,
        )

        return result

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail=f"Security test error: {error}",
        )


# -----------------------------
# Security Attack
# -----------------------------

@app.post("/security/attack")
async def run_security_attack(
    request: AttackRequest
):

    try:

        result = await security_engine.run_attack(
            attack_name=request.attack,
            provider=request.provider,
            model=request.model,
        )

        return result

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail=f"Security attack error: {error}",
        )


# -----------------------------
# Security Campaign
# -----------------------------

@app.post("/security/campaign")
async def run_security_campaign(
    request: CampaignRequest
):

    try:

        result = await security_campaign.run(
            attacks=request.attacks,
            provider=request.provider,
            model=request.model,
        )

        return result

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail=f"Security campaign error: {error}",
        )