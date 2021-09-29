import uuid

class Skill():
	def __init__(self, description: str
	, current_rank: int=1, desired_rank: int=5):
		self.id = uuid.uuid4()
		self.current_rank = current_rank
		self.desired_rank = desired_rank

class SkillsManager():
	def __init__(self):
		self.skills = []

	def add_skill(self, skill: Skill):
		self.skills.append(skill)

	def remove_skill(self, skill: Skill):
		self.skills.remove(skill)
