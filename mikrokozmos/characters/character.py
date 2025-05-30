from pydantic import BaseModel
from typing import List, Dict, Optional
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    # Gemini 1.5 Flash modelini kullan
    return genai.GenerativeModel("gemini-1.5-flash")

class Character(BaseModel):
    name: str
    bio: List[str]
    lore: List[str]
    knowledge: List[str]
    topics: List[str]
    style: Dict[str, List[str]]
    adjectives: List[str]
    modelProvider: str = "gemini"
    clients: List[str]

    @property
    def model(self):
        return get_gemini_model()

    def get_response(self, context: str, prompt: str) -> str:
        """Get character's response based on context and prompt"""
        system_prompt = f"""You are {self.name}. Here is your background:\nBio: {' '.join(self.bio)}\nKnowledge: {' '.join(self.knowledge)}\nStyle: {self.style['all']}\n\nRespond as this character would, maintaining their personality and knowledge base."""
        full_prompt = f"{system_prompt}\n\nContext: {context}\n\nPrompt: {prompt}"
        try:
            response = self.model.generate_content(
                full_prompt,
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.8,
                    "top_k": 40,
                    "max_output_tokens": 1024,
                }
            )
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "API key" in error_msg:
                return "[HATA]: Gemini API anahtarı bulunamadı veya geçersiz. Lütfen .env dosyasını kontrol edin."
            elif "model" in error_msg.lower():
                return "[HATA]: Model bulunamadı. Lütfen model adını kontrol edin."
            else:
                return f"[HATA]: {error_msg}"

    def react_to_event(self, event: str) -> str:
        """React to a specific event or situation"""
        return self.get_response(
            context="A new event has occurred in the village",
            prompt=f"How do you react to this event: {event}?"
        )

    def interact_with(self, other_character: 'Character', topic: str) -> str:
        """Interact with another character about a specific topic"""
        return self.get_response(
            context=f"You are talking with {other_character.name}",
            prompt=f"What would you say to {other_character.name} about {topic}?"
        ) 