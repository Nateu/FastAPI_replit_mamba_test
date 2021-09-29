from fastapi import FastAPI
from .skill_manager import Skill, SkillManager
# from typing import Optional
from pydantic import BaseModel

skill_manager = SkillManager
app = FastAPI()

host = "https://fastapi.nateucodes.repl.co/"

class SkillIn(BaseModel):
    description: str
    current_rank: int
    desired_rank: int 

@app.get("/")
def read_root():
    return {"skill_url": host + "skill/"}


@app.get("/skill/")
def read_skill():
    return {"skill": skill_manager.get_collection() }

@app.post("/skill/", response_model=SkillIn)
def add_skill(skill: SkillIn):
    new_skill = Skill(skill.description, skill.current_rank, skill.desired_rank)
    skill_manager.add_skill(new_skill)
    return {"skill": new_skill }

# @app.get("/skill/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
