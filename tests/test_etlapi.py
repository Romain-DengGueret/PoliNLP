import pytest
from polinlp.etl_api import etl_json_to_polarsdf
import polars as pl
from unittest.mock import patch


# Mocking the requests.get method to simulate an HTTP request
@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock_get:
        yield mock_get


def test_etl_json_to_polarsdf_is_function():
    # Checks taht 'etl_json_to_polarsdf' is a function
    assert callable(etl_json_to_polarsdf), "etl_json_to_polarsdf is not a function"


def test_etl_json_to_polarsdf_valid_response(mock_requests_get):
    # Simulate an HTTP 200 with a valid JSON
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = [
        {"key1": "value1", "key2": 2},
        {"key1": "value3", "key2": 4.0},
    ]

    # Call the function with a fictive url
    endpoint = "https://example.com/api/data"
    df = etl_json_to_polarsdf(endpoint)

    # Checks that we have a Polars DataFrame
    assert isinstance(df, pl.DataFrame), "The output is not a Polars DataFrame"

    # Checks that the http request status is 200
    mock_requests_get.assert_called_with(endpoint)
    assert (
        mock_requests_get.return_value.status_code == 200
    ), "The requests response is not 200"

    # Checks that the DataFrame contains the expected values
    assert df.shape == (2, 2), f"The DataFrame has a wrong shape : {df.shape}"
    assert df["key1"].to_list() == ["value1", "value3"], "'key1' values are wrong"
    assert df["key2"].to_list() == [2.0, 4.0], "'key2' values are wrong"
