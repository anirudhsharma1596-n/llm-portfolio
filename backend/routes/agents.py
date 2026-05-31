
from fastapi import APIRouter
from pydantic import BaseModel,Field



router = APIRouter()

class Steps(BaseModel):
    steps:int
    model_output:str
    tool_called:str
    observation:str


class ReactRequest(BaseModel):
    question:str


class ReactResponse(BaseModel):
    technique:str|None=Field(default="ReAct")
    question:str
    steps:list[Steps]
    final_answer:str


@router.post("/react",response_model=ReactResponse)
def react(req:ReactRequest):
    #todo
    return ReactResponse(
        question=req.question,
        steps=[Steps(
            steps=4,
            model_output="test",
            tool_called="test",
            observation="test"
        )],
        final_answer="test"
    )


class Agents(BaseModel):
    agent:str
    role:str
    input:str
    output:str


class MultiAgentRequest(BaseModel):
    topic:str


class MultiAgentResponse(BaseModel):
    technique:str|None=Field(default="Multi-agent")
    topic:str
    agents:list[Agents]


@router.post("/multi-agent",response_model=MultiAgentResponse)
def multi_agent(req:MultiAgentRequest):
    #todo
    return MultiAgentResponse(
        topic=req.topic,
        agents=[
            Agents(
                agent="test",
                role="test",
                input="test",
                output="test"
            )
        ]
    )
