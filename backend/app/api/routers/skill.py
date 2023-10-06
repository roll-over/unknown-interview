from fastapi import APIRouter

from app.api.schemas.skill import SkillSchema
from app.services.repository import SkillsRepository

skill_router = APIRouter(prefix="/skills", tags=["Skills"])


@skill_router.get("/", response_model=list[SkillSchema])
async def get_all_skills(Skill: SkillsRepository, limit: int = 10):
    return await Skill.get_all_skills(limit)


@skill_router.post("/", response_model=SkillSchema)
async def post_skill(skill: SkillSchema, Skill: SkillsRepository):
    return await Skill.create_one(skill)
