from typing import Union


class RiskScore:
    INSURANCE_LINES = set(["auto", "disability", "home", "life"])
    FINAL_SCORES = set(["ineligible", "economic", "regular", "responsible"])

    def __init__(self):
        self.__risk_score = {line: 0 for line in RiskScore.INSURANCE_LINES}

    @property
    def risk_score(self) -> dict[str, int]:
        return self.__risk_score

    @risk_score.setter
    def risk_score(self, increments: dict[str, Union[int, str]]) -> None:
        for insurance_line in RiskScore.INSURANCE_LINES & increments.keys():
            update = increments[insurance_line]
            if update in RiskScore.FINAL_SCORES:
                # ineligibility is an unchangeable state for each particular line
                if self.__risk_score[insurance_line] != "ineligible":
                    self.__risk_score[insurance_line] = update
            elif type(update) == int:
                self.__risk_score[insurance_line] += update

    def risk_score_update(self, increments: dict[str, int]) -> dict[str, int]:
        self.risk_score = increments
        return self.__risk_score

    def calc_final(self, score: Union[int, str]) -> str:
        if score == "ineligible":
            return score
        elif score <= 0:
            return "economic"
        elif score in [1, 2]:
            return "regular"
        elif score >= 3:
            return "responsible"
        else:
            # raise error and or log, this shouldn't happen
            pass

    def view_final(self) -> dict[str, str]:
        """
        Does not modify score, just returns "view" of current assessment.
        """
        print(f"final risk sore numeric: {self.risk_score}")
        score_view = {
            line: self.calc_final(self.risk_score[line])
            for line in RiskScore.INSURANCE_LINES
        }
        return score_view
