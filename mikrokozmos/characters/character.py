from pydantic import BaseModel
from typing import List, Dict
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model():
    """Gemini modelini yapılandırır ve döndürür."""
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        return genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print(f"Model yapılandırma hatası: {str(e)}")
        return None

class Character(BaseModel):
    name: str
    bio: str
    lore: str
    knowledge: List[str]
    topics: List[str]
    style: str
    adjectives: List[str]
    clients: List[str] = []
    modelProvider: str = "gemini"

    @property
    def model(self):
        """Gemini modelini döndürür."""
        return get_gemini_model()

    def get_response(self, context: str, prompt: str) -> str:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(
                f"""Karakter: {self.name}
                Biyografi: {self.bio}
                Arka Plan: {self.lore}
                Bilgi: {', '.join(self.knowledge)}
                Konular: {', '.join(self.topics)}
                Konuşma Tarzı: {self.style}
                Özellikler: {', '.join(self.adjectives)}
                
                Bağlam: {context}
                
                Sohbet: {prompt}""",
                generation_config={
                    'temperature': 0.7,
                    'top_p': 0.8,
                    'top_k': 40,
                    'max_output_tokens': 1024,
                }
            )
            return response.text
        except Exception as e:
            if "API key" in str(e):
                return f"Hata: Gemini API anahtarı bulunamadı. Lütfen .env dosyasında GEMINI_API_KEY değişkenini ayarlayın."
            elif "model" in str(e):
                return f"Hata: Gemini modeli bulunamadı. Lütfen model adını kontrol edin."
            else:
                return f"Hata: {str(e)}"

    def react_to_event(self, event: str) -> str:
        return self.get_response(
            context=f"Gündemdeki olay: {event}",
            prompt=f"Bu olay hakkında ne düşünüyorsun ve nasıl tepki veriyorsun?"
        )

    def interact_with(self, other_character: 'Character', context: str) -> str:
        return self.get_response(
            context=f"Diğer karakter: {other_character.name}\nGündemdeki konu: {context}",
            prompt=f"{other_character.name} ile bu konu hakkında nasıl bir diyalog kurarsın?"
        ) 