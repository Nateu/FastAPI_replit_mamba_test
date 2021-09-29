from mamba import describe, context, it, before
from expects import expect, equal
from fastapi.testclient import TestClient
from api import app, host

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
        with it("should return skills_url"):
            response = self.client.get("/skill")
            expect(response.status_code).to(equal(200))
            # expect(response.json()).to(equal({"skills_url": host + "skills/"}))
