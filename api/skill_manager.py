from typing import List
import uuid
import json


class Skill:
    def __init__(self,
                 description: str,
                 current_rank: int = 1,
                 desired_rank: int = 5):
        self.id = uuid.uuid4()
        self.description = description
        self.current_rank = current_rank
        self.desired_rank = desired_rank

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __repr__(self):
        return "%s, %s, %i, %i" % (self.id, self.description, self.current_rank, self.desired_rank)

class SkillManager:
    def __init__(self):
        self.collection = []

    def add_skill(self, skill: Skill):
        self.collection.append(skill)

    def remove_skill(self, skill: Skill):
        self.collection.remove(skill)

    def get_collection(self) -> List[Skill]:
        return self.collection

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
