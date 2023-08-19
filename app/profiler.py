from app.models.dataclass_models import PersonalInfoDataClass
from app.models.pydantic_models import OwnershipStatusPayloadEnum, MaritalStatusPayloadEnum
from datetime import datetime, timedelta

class Profiler:

    insurance_lines = ['life', 'disability', 'home', 'auto']

    def __init__(self, personal_info: PersonalInfoDataClass):
        self.personal_info = personal_info

    def calc_base_score(self):
        return sum(self.personal_info.risk_questions)

    def calc_risk_score_by_insurance_line(self) -> dict[str, str]:
        base_score = self.calc_base_score()
        risk_score = {
            "auto": base_score,
            "disability": base_score,
            "home": base_score,
            "life": base_score
        }

        # Criteria resulting in numerically incremented scores

        # user age
        if self.personal_info.age < 30:
            risk_score = {k: v-2 for k, v in risk_score.items()}
        elif 30 <= self.personal_info.age <= 40:
            risk_score = {k: v-1 for k, v in risk_score.items()}

        # income
        if self.personal_info.income > 200_000:
            risk_score = {k: v-1 for k, v in risk_score.items()}

        # house
        if self.personal_info.house.ownership_status == OwnershipStatusPayloadEnum.MORTGAGED:
            risk_score['disability'] += 1
            risk_score['home'] += 1

        # dependents
        if self.personal_info.dependents > 0:
            risk_score['disability'] += 1
            risk_score['life'] += 1

        # marriage
        if self.personal_info.marital_status.marital_status == MaritalStatusPayloadEnum.MARRIED:
            risk_score['life'] += 1
            risk_score['disability'] -= 1

        # TODO: vehicle
        # five_years_ago
        # if self.personal_info.vehicle.year > ()


        # Criteria resulting in categorical determinations of scores
        # If the user doesn’t have income, vehicles or houses, she is ineligible for disability, auto, and home insurance, respectively.


        # If the user is over 60 years old, she is ineligible for disability and life insurance.
        
        return risk_score
    