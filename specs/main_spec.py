from mamba import describe, context, it, before, after
from expects import expect, equal
from fastapi.testclient import TestClient
from mockito import when, unstub
from api import app, host, Skill, SkillManager
import uuid

FAKE_UUID = "-some-uuid-"

with describe("Given the end point /") as self:
    with before.each:
        self.client = TestClient(app)

    with context("when the endpoint is called with the get verb"):
        with it("should return skill_url"):
            response = self.client.get("/")
            expect(response.status_code).to(equal(200))
            expect(response.json()).to(equal({"skill_url": host + "skill/"}))

with describe("Given the resource /skill") as self:
    with before.each:
        self.client = TestClient(app)

    with context("when the endpoint is called with the get verb"):
        with before.each:
            when(SkillManager).get_collection(...).thenReturn([])

        with after.each:
            unstub()

        with it("should return an empty collection"):
            response = self.client.get("/skill")
            expect(response.status_code).to(equal(200))
            expect(response.json()).to(equal({'skill': []}))

    with context("when a skill is in the collection"):
        with before.each:
            when(uuid).uuid4(...).thenReturn(FAKE_UUID)
            self.skill = Skill(description="bluffing")
            when(SkillManager).get_collection(...).thenReturn([self.skill.to_json()])

        with it("should return an empty collection"):
            response = self.client.get("/skill")
            expect(response.status_code).to(equal(200))
            expect(response.json()).to(equal({'skill': [self.skill.to_json()]}))
