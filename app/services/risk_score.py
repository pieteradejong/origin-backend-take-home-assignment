from typing import Union

class RiskScore:
    INSURANCE_LINES = set(['auto', 'disability', 'home', 'life'])
    FINAL_SCORES = set(['ineligible', 'economic', 'regular', 'responsible'])
    # TODO: potentially add validation logic to ensure __risk_score never has fields other than these

    def __init__(self):
        self.__risk_score = { line: 0 for line in RiskScore.INSURANCE_LINES }

    @property
    def risk_score(self) -> dict[str, int]:
        return self.__risk_score
    
    @risk_score.setter
    def risk_score(self, increments: dict[str, int]) -> None:
        for insurance_line, incr in increments.items():
            if insurance_line not in RiskScore.INSURANCE_LINES:
                # TODO log attempted to increment score for insurance line unknown to RiskScore
                # maybe raise value error
                continue
            else:
                if self.__risk_score[insurance_line] not in RiskScore.FINAL_SCORES:
                    self.__risk_score[insurance_line] += incr
        
    
    def risk_score_update(self, increments: dict[str, int]) -> dict[str, int]:
        self.risk_score = increments
        return self.__risk_score


    def calc_final(score: Union[int, str]) -> str:
        if score == 'ineligible': return score
        elif score <= 0: return 'economic'
        elif score in [1,2]: return 'regular'
        elif score >= 3: return 'responsible'
        else:
            # raise error and or log, this shouldn't happen
            pass

    def view_final(self) -> dict[str, str]:
        """
        Does not modify score, just returns "view" of current assessment.
        """
        score_view = { line: self.calc_final(self.risk_score[line]) for line in RiskScore.INSURANCE_LINES }
        return score_view
        
            

