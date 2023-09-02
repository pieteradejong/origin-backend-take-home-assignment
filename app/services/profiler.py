from app.models.dataclass_models import PersonalInfoDataClass, MaritalStatus
from app.models.pydantic_models import OwnershipStatusPayloadEnum
from app.services.risk_score import RiskScore

class Profiler:

    # def calc_base_score(personal_info: PersonalInfoDataClass) -> int:
    #     return sum(personal_info.risk_questions)

    # @staticmethod
    # def generate_risk_profile(base_profile: dict[str, int], personal_info: PersonalInfoDataClass) -> dict[str, int]:
    #     pass
    #     risk_profile = {k: v for k, v in base_profile.items()}
        # call a series of private functions for each field (age, income, etc.),
        # and increment the risk profile accordingly
    
    @staticmethod
    def calc_risk_score(personal_info: PersonalInfoDataClass) -> dict[str, str]:

        risk_score = RiskScore()

        if personal_info.age < 30:
            risk_score.risk_score = {k: -2 for k in RiskScore.INSURANCE_LINES }
        elif 30 <= personal_info.age <= 40:
            risk_score.risk_score = {k: -1 for k in RiskScore.INSURANCE_LINES }

        if personal_info.income > 200_000:
            risk_score.risk_score = {k: -1 for k in RiskScore.INSURANCE_LINES }

        if personal_info.house.ownership_status == OwnershipStatusPayloadEnum.MORTGAGED:
            risk_score.risk_score = {k: 1 for k in ['disability', 'home']}

        if personal_info.dependents > 0:
            risk_score.risk_score = {k: 1 for k in ['disability', 'life']}

        if personal_info.marital_status == MaritalStatus.MARRIED:
            risk_score.risk_score = { 'life': 1, 'disability': -1 }

        # TODO: vehicle
        # five_years_ago
        # if self.personal_info.vehicle.year > ()

        # Criteria resulting in categorical determinations of scores
        # If the user doesn’t have income, vehicles or houses, she is ineligible for disability, auto, and home insurance, respectively.


        # If the user is over 60 years old, she is ineligible for disability and life insurance.

        return risk_score.view_final()
    
    