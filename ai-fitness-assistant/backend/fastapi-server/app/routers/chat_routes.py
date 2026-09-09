from fastapi import APIRouter
from pydantic import BaseModel
from ai_models.chatbot.gemini_bot import gemini_bot

router = APIRouter(
    prefix="/chat",
    tags=["Chatbot"]
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/ask", response_model=ChatResponse)
async def ask_chatbot(request: ChatRequest):
    """
    Endpoint to receive a user message and return an AI-generated fitness response.
    """
    reply_text = gemini_bot.ask(request.message)
    return ChatResponse(reply=reply_text)
