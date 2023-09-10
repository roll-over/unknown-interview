from app.repository.services import VacancyCVNoteService
from app.repository.interfaces import MongoBeanieRepository
from app.db.models.vacancy_note import VacancyNote
from app.db.models.mixins import Note


class VacancyNoteRepositoryModel(MongoBeanieRepository):
    model = VacancyNote


def get_vacancy_note_repository():
    return VacancyCVNoteService(VacancyNoteRepositoryModel, Note)
