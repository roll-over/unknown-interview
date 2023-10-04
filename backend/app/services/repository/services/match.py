from typing import Dict, Union
from uuid import UUID

from app.db.models import CV, Match, MatchRelation, Vacancy
from app.services.repository.interfaces import AbstractBaseRepository


class MatchService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def add_records(self, data: Match) -> None:
        return await self.repo.create_many(data)

    async def get_records(
        self, data_id: Dict[str, UUID], limit: Union[int | None] = None
    ) -> Union[CV | Vacancy | None]:
        record = await self.repo.fetch_many(data_id, limit)

        if record:
            return record.pop()

    async def update_relation(
        self,
        data: Union[CV | Vacancy],
        relation: MatchRelation,
        new_relation_type: MatchRelation,
    ) -> Union[CV | Vacancy]:
        match relation:
            case "applicant_relation":
                data.applicant_relation = new_relation_type
            case "employer_relation":
                data.employer_relation = new_relation_type

        return await self.repo.update_one(data, {"custom_id": data.custom_id})
