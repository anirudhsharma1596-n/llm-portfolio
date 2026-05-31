
from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI

client=OpenAI()


router = APIRouter()

class PromptRequest(BaseModel):
    prompt:str


class CompareResult(BaseModel):
    technique:str
    description:str
    prompt_sent:list[dict]
    output:str

class CompareResponse(BaseModel):
    prompt:str
    results:list[CompareResult]


def call_llm(messages: list) -> str:
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=messages
    )
    return res.choices[0].message.content

@router.post("/zero-shot")
def zero_shot(request:PromptRequest):
    messages=[
            {"role":"user","content":request.prompt}
        ]
    response=call_llm(
        messages
    )

    return {
        "technique":"Zero-Shot",
        "prompt_sent":messages,
        "output":response
    }



@router.post("/compare")
def compare(request:PromptRequest):

    zero_messages = [
        {"role": "user", "content": request.prompt}
    ]

    few_messages = [
        {"role": "user",      "content": "Classify sentiment: 'I love this product!'"},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user",      "content": "Classify sentiment: 'Terrible experience.'"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user",      "content": "Classify sentiment: 'It was okay, nothing special.'"},
        {"role": "assistant", "content": "NEUTRAL"},
        {"role": "user",      "content": request.prompt}
    ]

    cot_messages = [
        {
            "role": "user",
            "content": f"{request.prompt}\nLet's think step by step."
        }
    ]

    r1=call_llm(zero_messages)
    r2=call_llm(few_messages)
    r3=call_llm(cot_messages)

    return{
        "prompt":request.prompt,
        "results":[
            CompareResult(
                technique="Zero shot",
                description="No examples, no guidance — the raw LLM answers purely from its training knowledge.",
                prompt_sent=zero_messages,
                output=r1
            ),
            CompareResult(
                technique="Few shot",
                description="3 examples shown before the question — teaches the model the exact format and style expected.",
                prompt_sent=few_messages,
                output=r2
            ),
            CompareResult(
                technique="Chain Of Thought",
                description="Forces the model to reason step by step before answering — dramatically improves accuracy on complex questions.",
                prompt_sent=cot_messages,
                output=r3
            )
        ]
        
    }
