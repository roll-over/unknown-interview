from typing import Dict, Tuple, Union
from uuid import UUID

from app.db.models import CV, Match, MatchRelation, Vacancy
from app.services.repository.interfaces import AbstractBaseRepository


class MatchService:
    def __init__(self, repo_model: AbstractBaseRepository):
        self.repo: AbstractBaseRepository = repo_model()

    async def add_records(self, data: Match) -> None:
        return await self.repo.create_many(data)

    async def get_records(
            self,
            data: Dict[str, UUID],
            sort: Tuple[str, int] = None,
            limit: Union[int | None] = None,
    ) -> Union[CV | Vacancy | None]:
        record = await self.repo.fetch_many(data, sort=sort, limit=limit)
        if record and limit:
            return record.pop()
        return record

    async def update_relation(
        self,
        data: Union[CV | Vacancy],
        relation: MatchRelation,
        new_relation_type: MatchRelation,
    ) -> Union[CV | Vacancy]:
        match relation:
            case "applicant_relation":
                updated_field = {"applicant_relation": new_relation_type}
            case "employer_relation":
                updated_field = {"employer_relation": new_relation_type}

        return await self.repo.update_one(updated_field, {"custom_id": data.custom_id})

    async def delete_matches(self, record_id):
        return await self.repo.delete_data(record_id)

    async def get_matches(self, filter_, limit=None):
        return await self.repo.fetch_many(filter_, limit)
