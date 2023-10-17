import pytest
from app.services.risk_score import RiskScore

@pytest.fixture
def zero_risk_score(mocker):
    mock_risk_profile = mocker.Mock()
    mock_risk_profile.risk_score = { line: 0 for line in RiskScore.INSURANCE_LINES }
    return mock_risk_profile


# def test_risk_score_with_ineligible_input():
#     # Arrange
#     risk_score_service = RiskScore()
#     ineligible_input = {'auto': 'ineligible'}  # 'auto' is one of the insurance lines

#     # Act
#     result = risk_score_service.risk_score_update(ineligible_input)

#     # Assert
#     # replace with your assertion. For example, if you expect the risk score to be updated with the ineligible input:
#     assert result['auto'] == 'ineligible'