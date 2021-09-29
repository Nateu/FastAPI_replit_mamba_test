from mamba import describe, context, it, before, after
from expects import expect, equal
from mockito import when, unstub
from api import Skill, SkillManager
import uuid

FAKE_UUID = "-some-uuid-"

with describe("Given a new skill 'bluffing'") as self:
    with before.each:
        when(uuid).uuid4(...).thenReturn(FAKE_UUID)
        self.skill = Skill(description="bluffing")

    with after.each:
        unstub()

    with context("when it is created"):
        with it("should get a uuid"):
            expect(self.skill.id).to(equal(FAKE_UUID))

        with it("should have a default value 1 for current_rank"):
            expect(self.skill.current_rank).to(equal(1))

        with it("should have a default value 5 for desired_rank"):
            expect(self.skill.desired_rank).to(equal(5))

    with context("when the method to_json is called"):
        with it("should return a JSON"):
            expect(self.skill.to_json()).to(
                equal('{"id": "-some-uuid-", "description": "bluffing", "current_rank": 1, "desired_rank": 5}'))

    with context("when it is printed"):
        with it("should return a string"):
            expect(f"{self.skill}").to(equal("-some-uuid-, bluffing, 1, 5"))

with describe("Given a SkillManager") as self:
    with before.each:
        self.skill_manager = SkillManager()

    with after.each:
        unstub()

    with context("when it is created"):
        with it("should be empty"):
            expect(self.skill_manager.get_collection()).to(equal([]))

    with context("when a skill is added"):
        with before.each:
            when(uuid).uuid4(...).thenReturn(FAKE_UUID)
            self.skill = Skill(description="bluffing")

        with it("should hold that skill"):
            self.skill_manager.add_skill(self.skill)
            expect(self.skill_manager.get_collection()).to(equal([self.skill]))

        with context("and to_json is called"):
            with it("should show a json collection"):
                self.skill_manager.add_skill(self.skill)
                expect(self.skill_manager.to_json()).to(equal('{"collection": [{"id": "-some-uuid-", "description": "bluffing", "current_rank": 1, "desired_rank": 5}]}'))

    with context("when a skill is removed"):
        with before.each:
            when(uuid).uuid4(...).thenReturn(FAKE_UUID)
            self.skill = Skill(description="bluffing")
            self.skill_manager.add_skill(self.skill)

        with it("should hold that skill"):
            self.skill_manager.remove_skill(self.skill)
            expect(self.skill_manager.get_collection()).to(equal([]))

