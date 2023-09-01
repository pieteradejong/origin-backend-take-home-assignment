from app.models.dataclass_models import PersonalInfoDataClass
from app.models.pydantic_models import OwnershipStatusPayloadEnum, MaritalStatusPayloadEnum
from typing import Callable, List

class Profiler:

    insurance_lines = ['life', 'disability', 'home', 'auto']
    scoring_rules: List[Callable] = [income_score]

    def income_score(intermediate_score: dict[str, int], personal_info: PersonalInfoDataClass) -> dict[str, int]:
        if personal_info.income > 200_000:
            intermediate_score = {k: v-1 for k, v in intermediate_score.items()}
        return intermediate_score

    def calc_base_score(personal_info: PersonalInfoDataClass) -> int:
        return sum(personal_info.risk_questions)

    @staticmethod
    def generate_base_profile(base_score: int, insurance_lines: list = insurance_lines) -> dict[str, int]:
        return {line: 0 + base_score for line in insurance_lines}

    @staticmethod
    def generate_risk_profile(base_profile: dict[str, int], personal_info: PersonalInfoDataClass) -> dict[str, int]:
        pass
        risk_profile = {k: v for k, v in base_profile.items()}
        # call a series of private functions for each field (age, income, etc.),
        # and increment the risk profile accordingly
    
    @staticmethod
    def calc_risk_score(base_profile: dict[str, int], personal_info: PersonalInfoDataClass) -> dict[str, str]:
        # Criteria resulting in numerically incremented scores

        if personal_info.age < 30:
            risk_score = {k: v-2 for k, v in risk_score.items()}
        elif 30 <= personal_info.age <= 40:
            risk_score = {k: v-1 for k, v in risk_score.items()}

        if personal_info.income > 200_000:
            risk_score = {k: v-1 for k, v in risk_score.items()}

        if personal_info.house.ownership_status == OwnershipStatusPayloadEnum.MORTGAGED:
            risk_score['disability'] += 1
            risk_score['home'] += 1

        if personal_info.dependents > 0:
            risk_score['disability'] += 1
            risk_score['life'] += 1

        if personal_info.marital_status.marital_status == MaritalStatusPayloadEnum.MARRIED:
            risk_score['life'] += 1
            risk_score['disability'] -= 1

        # TODO: vehicle
        # five_years_ago
        # if self.personal_info.vehicle.year > ()


        # Criteria resulting in categorical determinations of scores
        # If the user doesn’t have income, vehicles or houses, she is ineligible for disability, auto, and home insurance, respectively.


        # If the user is over 60 years old, she is ineligible for disability and life insurance.
        
        return risk_score
    