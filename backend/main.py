from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes import prompting, rag, agents, safety

load_dotenv()

app = FastAPI(title="Anirudh Sharma — AI Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all route groups
app.include_router(prompting.router, prefix="/prompting", tags=["Prompting"])
app.include_router(rag.router,       prefix="/rag",       tags=["RAG & Memory"])
app.include_router(agents.router,    prefix="/agents",    tags=["Agents"])
app.include_router(safety.router,    prefix="/safety",    tags=["Safety & Eval"])

@app.get("/health")
def health():
    return {"status": "ok"}