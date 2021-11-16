# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
import requests_mock

from GrantaBomSvcs.api.documentation_api import DocumentationApi  # noqa: E501
from .common import generate_model, get_example


class TestDocumentationApi():
    """DocumentationApi unit test stubs"""


    @pytest.mark.xfail(reason="No example payload in API definition")
    def test_get_miservicelayer_bom_analytics_v1svc_yaml(self, api_client):
        """Test case for get_miservicelayer_bom_analytics_v1svc_yaml

        Provides the YAML specification for this service.  # noqa: E501
        """
        client = DocumentationApi(api_client)
        with requests_mock.Mocker() as m:
            m.post('http://localhost/mi_servicelayer/BomAnalytics/v1.svc/yaml', json=get_example(str))
            result = client.get_miservicelayer_bom_analytics_v1svc_yaml()
        assert isinstance(result, str)

