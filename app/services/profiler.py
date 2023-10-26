from app.models.dataclass_models import PersonalInfoDataClass, MaritalStatus
from app.models.pydantic_models import OwnershipStatusPayloadEnum
from app.services.risk_score import RiskScore
from datetime import date


class Profiler:
    @staticmethod
    def calc_risk_score(personal_info: PersonalInfoDataClass) -> dict[str, str]:
        risk_score = RiskScore()

        # Apply base score based risk questions
        risk_score.risk_score = {
            k: sum(personal_info.risk_questions) for k in RiskScore.INSURANCE_LINES
        }

        if personal_info.age < 30:
            risk_score.risk_score = {k: -2 for k in RiskScore.INSURANCE_LINES}
        elif 30 <= personal_info.age <= 40:
            risk_score.risk_score = {k: -1 for k in RiskScore.INSURANCE_LINES}

        if personal_info.income > 200_000:
            risk_score.risk_score = {k: -1 for k in RiskScore.INSURANCE_LINES}

        if personal_info.house:
            if (
                personal_info.house.ownership_status
                == OwnershipStatusPayloadEnum.MORTGAGED
            ):
                risk_score.risk_score = {k: 1 for k in ["disability", "home"]}

        if personal_info.dependents > 0:
            risk_score.risk_score = {k: 1 for k in ["disability", "life"]}

        if personal_info.marital_status == MaritalStatus.MARRIED:
            risk_score.risk_score = {"life": 1, "disability": -1}

        if not personal_info.vehicle:
            risk_score.risk_score = {"auto": "ineligible"}
        else:
            # Requirement is 'was produced in the last 5 years'
            # Implementation obv assumes not to mean 'rolling 5*12mo basis',
            # since in Dev 2023, Jan 2018 is still 'within 5 years.'
            curr_year = date.today().year
            if personal_info.vehicle.year >= curr_year - 5:
                risk_score.risk_score = {k: 1 for k in ["auto"]}

        if personal_info.income == 0:
            risk_score.risk_score = {"disability": "ineligible"}

        if not personal_info.house:
            risk_score.risk_score = {"house": "ineligible"}
            print(f'income: home is ineligible')

        if personal_info.age > 60:
            risk_score.risk_score = {"disability": "ineligible", "life": "ineligible"}

        return risk_score.view_final()
