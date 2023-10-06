from app.db.models.cv_note import CVNote
from app.db.models.mixins import Note
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import VacancyCVNoteService


class CVNoteRepositoryModel(MongoBeanieRepository):
    model = CVNote


def get_cv_note_repository():
    return VacancyCVNoteService(CVNoteRepositoryModel, Note)
