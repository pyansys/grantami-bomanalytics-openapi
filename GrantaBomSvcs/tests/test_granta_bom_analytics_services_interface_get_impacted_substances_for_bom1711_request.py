# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pytest  # noqa: F401
from GrantaBomSvcs.models import GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request  # noqa: E501
from .common import generate_model



def test_GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request():
    """Test GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request"""

    model = generate_model(GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request)
    assert model
