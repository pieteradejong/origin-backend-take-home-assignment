from app.models.dataclass_models import PersonalInfoDataClass

class Profiler:

    insurance_lines = ['life', 'disability', 'home', 'auto']

    def __init__(self, personal_info: PersonalInfoDataClass):
        self.personal_info = personal_info

    def calc_base_score(self):
        return sum(self.personal_info.risk_questions)


