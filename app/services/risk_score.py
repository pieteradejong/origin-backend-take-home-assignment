from typing import Union


class RiskScore:
    INSURANCE_LINES = set(["auto", "disability", "home", "life"])
    FINAL_SCORES = set(["ineligible", "economic", "regular", "responsible"])
    # TODO: Separate set of IRREVERISBLE SCORES, incl for now only "ineligible"

    def __init__(self):
        self.__risk_score = {line: 0 for line in RiskScore.INSURANCE_LINES}

    @property
    def risk_score(self) -> dict[str, int]:
        return self.__risk_score

    @risk_score.setter
    def risk_score(self, increments: dict[str, Union[int, str]]) -> None:
        for insurance_line in RiskScore.INSURANCE_LINES & increments.keys():
            if self.__risk_score[insurance_line] == "ineligible":
                continue

            update = increments[insurance_line]

            if update in RiskScore.FINAL_SCORES:
                self.__risk_score[insurance_line] = update
            else:
                self.__risk_score[insurance_line] += update

    # TODO rename to `update`
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
            # TODO raise and or log
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
        print(f"score view: {score_view}")
        return score_view
