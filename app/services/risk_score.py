from enum import Enum

class InsuranceLines(Enum):
    AUTO = "auto"
    DISABILITY = "disability"
    HOME = "home"
    LIFE = "life"

class RiskScore:
    INSURANCE_LINES = set('auto', 'disability', 'home', 'life')
    # TODO: potentially add validation logic to ensure __risk_score never has fields other than these

    def __init__(self):
        # self.__risk_score = { line.value: 0 for line in InsuranceLines.items }
        self.__risk_score = { line.value: 0 for line in RiskScore.INSURANCE_LINES }

    @property
    def risk_score(self) -> dict[str, int]:
        return self.__risk_score
    
    def increment(self, increments: dict[str, int]) -> dict[str, int]:
        for line, incr in increments.items():
            if line not in RiskScore.INSURANCE_LINES:
                # TODO log attempted to increment score for insurance line unknown to RiskScore
                pass
            else:
                # TODO check if score is already "ineligiible", skip if so
                self.__risk_score[line] += incr

        return self.__risk_score        

    def finalize(self) -> dict[str, str]:
        for line in RiskScore.INSURANCE_LINES:
            

