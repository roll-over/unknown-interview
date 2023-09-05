from app.repository.services import VacancyCVNoteService
from app.repository.interfaces import MongoBeanieRepository
from app.db.models.cv_note import CVNote
from app.db.models.mixins import Note


class CVNoteRepositoryModel(MongoBeanieRepository):
    model = CVNote


def get_cv_note_repository():
    return VacancyCVNoteService(CVNoteRepositoryModel, Note)
