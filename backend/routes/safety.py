
from fastapi import APIRouter
from pydantic import BaseModel,Field
from enum import Enum

router = APIRouter()

class Stage(Enum):
    GENERATE="Generate"
    CRITIQUE="Critique"
    REVISE="Revise"


class ConstitutionalStage(BaseModel):
    stage:Stage|None=Stage.GENERATE
    output:str

class ConstitutionalRequest(BaseModel):
    prompt:str
    constitution:list[str]

class ConstitutionalResponse(BaseModel):
    technique:str|None=Field(default="Constitutional AI")
    prompt:str
    constitution:str
    stages:list[ConstitutionalStage]

@router.post("/constitutional",response_model=ConstitutionalResponse)
def constitutional(req:ConstitutionalRequest):
    return ConstitutionalResponse(
        prompt="test",
        constitution="test",
        stages=[
            ConstitutionalStage(
                output="test"
            )
        ]
    )
   

class HallucinationrRisk(Enum):
    LOW="Low"
    MEDIUM="Medium"
    HIGH="High"

class HallucinationCheckRequest(BaseModel):
    prompt:str

class HallucinationCheckResponse(BaseModel):
    technique:str|None=Field(default="Hallucination Detection")
    prompt:str
    response_1:str
    response_2:str
    response_3:str
    consistent:bool
    hallucination_risk:HallucinationrRisk|None=HallucinationrRisk.LOW
    contradictions:list[str]
    reasoning:str

@router.post("/hallucination-check",response_model=HallucinationCheckResponse)
def hallucination_risk(req:HallucinationCheckRequest):
    return HallucinationCheckResponse(
        prompt="test",
        response_1="test",
        response_2="test",
        response_3="test",
        consistent=True,
        contradictions=["test","test"],
        reasoning="test"
    )


class SycopahancyCheckTurn(BaseModel):
    turn:int
    user_message:str
    model_response:str

class SycopahancyCheckRequest(BaseModel):
    claim:str


class SycopahancyCheckResponse(BaseModel):
    technique:str|None=Field(default="Hallucination Detection")
    claim:str
    turns:list[SycopahancyCheckTurn]
    verdict:str
    sycophancy_detected:bool


@router.post("/sycophancy-check",response_model=SycopahancyCheckResponse)
def sycophancy_risk(req:SycopahancyCheckRequest):
    return SycopahancyCheckResponse(
        claim="test",
        turns=[
            SycopahancyCheckTurn(
                turn=1,
                user_message="test",
                model_response="test"
            )
        ],
        verdict="test",
        sycophancy_detected=True
    )

