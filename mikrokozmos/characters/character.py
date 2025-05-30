from pydantic import BaseModel
from typing import List, Dict
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

def get_gemini_model():
    """Gemini modelini yapılandırır ve döndürür."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY bulunamadı. Lütfen .env dosyasını kontrol edin.")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        return model
    except Exception as e:
        logger.error(f"Model yapılandırma hatası: {str(e)}")
        raise

class Character(BaseModel):
    name: str
    bio: List[str]
    lore: List[str]
    knowledge: List[str]
    topics: List[str]
    style: Dict[str, List[str]]
    adjectives: List[str]
    clients: List[str] = []
    modelProvider: str = "gemini"

    @property
    def model(self):
        """Gemini modelini döndürür."""
        return get_gemini_model()

    def get_response(self, context: str, prompt: str) -> str:
        try:
            model = get_gemini_model()
            response = model.generate_content(
                f"""Karakter: {self.name}
                Biyografi: {' '.join(self.bio)}
                Arka Plan: {' '.join(self.lore)}
                Bilgi: {', '.join(self.knowledge)}
                Konular: {', '.join(self.topics)}
                Konuşma Tarzı: {', '.join(self.style['all'])}
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
            error_msg = str(e)
            if "API key" in error_msg:
                return "Hata: Gemini API anahtarı bulunamadı veya geçersiz. Lütfen .env dosyasını kontrol edin."
            elif "model" in error_msg.lower():
                return "Hata: Model bulunamadı. Lütfen model adını kontrol edin."
            else:
                logger.error(f"Karakter yanıt hatası: {error_msg}")
                return f"Hata: {error_msg}"

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