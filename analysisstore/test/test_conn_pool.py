from ..client.commands import AnalysisClient
from .conftest import testing_config
import pytest


def test_client_badconf():
    config = {"host": "localhost"}
    pytest.raises(KeyError, AnalysisClient, config)
    config["port"] = testing_config["port"]
    config["use_ssl"] = testing_config["use_ssl"]
    client = AnalysisClient(config)
