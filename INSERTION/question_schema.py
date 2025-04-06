from typing import Optional, List
from pydantic import BaseModel

class Option(BaseModel):
    is_image: bool
    is_latex: bool
    text: Optional[str]
    latex_string: Optional[str]
    image_url: Optional[str]
    is_correct: bool

class Question(BaseModel):
    id: str
    type: str
    text: str
    is_latex: bool
    is_image: bool
    image_url: Optional[str]
    latex_string: Optional[str]
    xp: int
    tag: Optional[str]
    difficulty: str
    topic: str
    chapter: str
    option_list: List[Option]
