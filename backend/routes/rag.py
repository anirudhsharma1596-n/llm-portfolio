
from fastapi import APIRouter
from pydantic import BaseModel
from utils import OpenAIMessage

router = APIRouter()

class AskRequest(BaseModel):
    question:str
    context:str

class RagResponse(BaseModel):
    technique:str
    question:str|None=None
    context_used:str|None=None
    prompt_sent:OpenAIMessage
    output:str
    history_length:int|None=None
    message:str|None=None

class MemoryChatRequest(BaseModel):
    message:str
    history:list[OpenAIMessage]

@router.post("/ask",response_model=RagResponse,response_model_exclude_none=True)
def ask(req:AskRequest):
    #todo
    return RagResponse(
        technique="RAG",
        question="test_question",
        context_used="test context",
        prompt_sent=OpenAIMessage(role="user",content="test"),
        output=""
    )

@router.post("/memory-chat",response_model=RagResponse,response_model_exclude_none=True)
def memory_chat(req:MemoryChatRequest):
    #todo
    return RagResponse(
        technique="Memory Chat",
        prompt_sent=req.history[0],
        output="",
        history_length=0,
        message="test message"
    )
