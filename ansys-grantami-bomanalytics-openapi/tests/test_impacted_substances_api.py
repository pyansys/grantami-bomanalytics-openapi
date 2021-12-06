# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
import requests_mock

from ansys.grantami.bomanalytics_openapi.api.impacted_substances_api import ImpactedSubstancesApi  # noqa: E501
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_bom1711_request import GetImpactedSubstancesForBom1711Request
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_bom1711_response import GetImpactedSubstancesForBom1711Response
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_materials_request import GetImpactedSubstancesForMaterialsRequest
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_materials_response import GetImpactedSubstancesForMaterialsResponse
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_parts_request import GetImpactedSubstancesForPartsRequest
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_parts_response import GetImpactedSubstancesForPartsResponse
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_specifications_request import GetImpactedSubstancesForSpecificationsRequest
from ansys.grantami.bomanalytics_openapi.models.get_impacted_substances_for_specifications_response import GetImpactedSubstancesForSpecificationsResponse
from .common import generate_model, get_example


class TestImpactedSubstancesApi():
    """ImpactedSubstancesApi unit test stubs"""


    
    def test_post_impactedsubstances_bom1711(self, api_client):
        """Test case for post_impactedsubstances_bom1711

        Get the impacted substances for a BoM  # noqa: E501
        """
        model = generate_model(GetImpactedSubstancesForBom1711Request)
        client = ImpactedSubstancesApi(api_client)
        with requests_mock.Mocker() as m:
            m.post('http://localhost/mi_servicelayer/BomAnalytics/v1.svc/impacted-substances/bom1711', json=get_example(GetImpactedSubstancesForBom1711Response))
            result = client.post_impactedsubstances_bom1711(model)
        assert isinstance(result, GetImpactedSubstancesForBom1711Response)

    
    def test_post_impactedsubstances_materials(self, api_client):
        """Test case for post_impactedsubstances_materials

        Get the impacted substances for materials  # noqa: E501
        """
        model = generate_model(GetImpactedSubstancesForMaterialsRequest)
        client = ImpactedSubstancesApi(api_client)
        with requests_mock.Mocker() as m:
            m.post('http://localhost/mi_servicelayer/BomAnalytics/v1.svc/impacted-substances/materials', json=get_example(GetImpactedSubstancesForMaterialsResponse))
            result = client.post_impactedsubstances_materials(model)
        assert isinstance(result, GetImpactedSubstancesForMaterialsResponse)

    
    def test_post_impactedsubstances_parts(self, api_client):
        """Test case for post_impactedsubstances_parts

        Get the impacted substances for parts  # noqa: E501
        """
        model = generate_model(GetImpactedSubstancesForPartsRequest)
        client = ImpactedSubstancesApi(api_client)
        with requests_mock.Mocker() as m:
            m.post('http://localhost/mi_servicelayer/BomAnalytics/v1.svc/impacted-substances/parts', json=get_example(GetImpactedSubstancesForPartsResponse))
            result = client.post_impactedsubstances_parts(model)
        assert isinstance(result, GetImpactedSubstancesForPartsResponse)

    
    def test_post_impactedsubstances_specifications(self, api_client):
        """Test case for post_impactedsubstances_specifications

        Get the impacted substances for specifications  # noqa: E501
        """
        model = generate_model(GetImpactedSubstancesForSpecificationsRequest)
        client = ImpactedSubstancesApi(api_client)
        with requests_mock.Mocker() as m:
            m.post('http://localhost/mi_servicelayer/BomAnalytics/v1.svc/impacted-substances/specifications', json=get_example(GetImpactedSubstancesForSpecificationsResponse))
            result = client.post_impactedsubstances_specifications(model)
        assert isinstance(result, GetImpactedSubstancesForSpecificationsResponse)
