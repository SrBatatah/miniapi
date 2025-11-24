import pytest
from unittest.mock import patch, Mock
from src.services.exchange_service import get_usd_to_brl


def test_get_usd_to_brl_ok():
    fake_response = {
        "USDBRL": {
            "bid": "5.1234",
            "create_date": "2025-11-21 10:00:00",
        }
    }

    mock_resp = Mock()
    mock_resp.json.return_value = fake_response
    mock_resp.raise_for_status.return_value = None

    with patch("src.services.exchange_service.requests.get", return_value=mock_resp):
        result = get_usd_to_brl()

    assert result["pair"] == "USD-BRL"
    assert result["bid"] == 5.1234
    assert result["timestamp"] == "2025-11-21 10:00:00"


def test_get_usd_to_brl_bad_payload():
    mock_resp = Mock()
    mock_resp.json.return_value = {}
    mock_resp.raise_for_status.return_value = None

    with patch("src.services.exchange_service.requests.get", return_value=mock_resp):
        with pytest.raises(ValueError):
            get_usd_to_brl()
