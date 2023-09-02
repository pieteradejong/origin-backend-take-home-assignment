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


    def calc_final(self, score: Union[int, str]) -> str:
        # for a in arg:
        #     print(f"calc_final:  *arg: {a}")
        # print(f"expect to be 1=  {len(arg)}")
        # print(self.risk_sco)

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
        
        # for line in RiskScore.INSURANCE_LINES:
        #     print(f"expect to be one arg: [{self.risk_score[line]}]")
        score_view = { line: self.calc_final(self.risk_score[line]) for line in RiskScore.INSURANCE_LINES }
        return score_view
        
    # def get_final_score(risk_score: dict[str, int]) -> dict[str, str]:
    #     final = {line: '' for line in RiskScore.INSURANCE_LINES}
        
    #     for l in RiskScore.INSURANCE_LINES:
    #         score = risk_score
    #         # risk_score.

            

