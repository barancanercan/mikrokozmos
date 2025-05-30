from typing import Dict, List
from ..characters.character import Character
import json
import os

class CharacterService:
    def __init__(self):
        self.characters: Dict[str, Character] = {}
        self.load_characters()
    
    def load_characters(self):
        """Load all characters from JSON files"""
        characters_dir = os.path.join(os.path.dirname(__file__), '../characters/data')
        for filename in os.listdir(characters_dir):
            if filename.endswith('.json'):
                with open(os.path.join(characters_dir, filename), 'r', encoding='utf-8') as f:
                    char_data = json.load(f)
                    character = Character(**char_data)
                    self.characters[character.name] = character
    
    def get_character(self, name: str) -> Character:
        """Get a specific character by name"""
        return self.characters.get(name)
    
    def get_all_characters(self) -> List[Character]:
        """Get all characters"""
        return list(self.characters.values())
    
    def get_character_names(self) -> List[str]:
        """Get names of all characters"""
        return list(self.characters.keys()) 