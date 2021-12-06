# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest
import requests_mock
import ansys.openapi.common as auth
import ansys.grantami.bomanalytics_openapi.models as models


@pytest.fixture(scope="session")
def api_client():
    test_url = "http://localhost/mi_servicelayer/BomAnalytics/v1.svc"
    with requests_mock.Mocker() as m:
        m.get(test_url, status_code=200)
        api_client = auth.ApiClientFactory(test_url).with_anonymous().build()
        api_client.setup_client(models)
    return api_client