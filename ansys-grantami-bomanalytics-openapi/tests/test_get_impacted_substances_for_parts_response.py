# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from ansys.grantami.bomanalytics_openapi.models import GetImpactedSubstancesForPartsResponse  # noqa: E501
from .common import generate_model



def test_GetImpactedSubstancesForPartsResponse():
    """Test GetImpactedSubstancesForPartsResponse"""

    model = generate_model(GetImpactedSubstancesForPartsResponse)
    assert model

