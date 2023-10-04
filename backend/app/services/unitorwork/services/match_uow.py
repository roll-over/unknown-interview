from app.repository.repositories import cv_repo, match_repo, vacancy_repo


class UserVacancyCVUoW:
    def __init__(self):
        self.matches = match_repo()
        self.cvs = cv_repo()
        self.vacancies = vacancy_repo()
