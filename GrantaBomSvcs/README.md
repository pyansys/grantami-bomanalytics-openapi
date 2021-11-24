# GrantaBomSvcs
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: V1
- Package version: 1.0.0
- Build package: com.ansys.granta.codegen.AnsysPythonClientCodegen


## Requirements.

- Python 3.6+
- auth-common
- requests >= 2.26.0
- python-dateutil >= 2.8.2


## Installation & Usage

The GrantaBomSvcs package is hosted on pypi as a component of PyAnsys. Just use pip to install the latest available version:

```
pip install GrantaBomSvcs
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import GrantaBomSvcs
from ansys.openapi.common import ApiClientFactory, ApiException
from pprint import pprint

# Create a generic ApiClient and initialize with the relevant models
client = (
    ApiClientFactory('http://localhost/mi_servicelayer')
    .with_credentials(username='USERNAME', password='PASSWORD')
    .build()
)
client.setup_client(GrantaBomSvcs.models)

# create an instance of the API class
api_instance = GrantaBomSvcs.DocumentationApi(client)

try:
    # Provides the YAML specification for this service
    api_response = api_instance.get_miservicelayer_bom_analytics_v1svc_yaml()
    pprint(api_response)
except ApiException as e:
    print(f"Exception when calling DocumentationApi->get_miservicelayer_bom_analytics_v1svc_yaml:{e}\n")
```


## Authorization and Authentication

The example above will use Windows Authentication, with a fall back to Basic Authentication if it is not available. See
the documentation for the ansys-openapi-common package for more details on available authentication and authorization
options.


## API Endpoints

All URIs are relative to *http://localhost/mi_servicelayer*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ComplianceApi* | [**post_miservicelayer_bom_analytics_v1svc_compliance_bom1711**](docs/ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_bom1711) | **POST** /BomAnalytics/v1.svc/compliance/bom1711 | Get the compliance for a BoM
*ComplianceApi* | [**post_miservicelayer_bom_analytics_v1svc_compliance_materials**](docs/ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_materials) | **POST** /BomAnalytics/v1.svc/compliance/materials | Get compliance for materials
*ComplianceApi* | [**post_miservicelayer_bom_analytics_v1svc_compliance_parts**](docs/ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_parts) | **POST** /BomAnalytics/v1.svc/compliance/parts | Get compliance for parts
*ComplianceApi* | [**post_miservicelayer_bom_analytics_v1svc_compliance_specifications**](docs/ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_specifications) | **POST** /BomAnalytics/v1.svc/compliance/specifications | Get compliance for specifications
*ComplianceApi* | [**post_miservicelayer_bom_analytics_v1svc_compliance_substances**](docs/ComplianceApi.md#post_miservicelayer_bom_analytics_v1svc_compliance_substances) | **POST** /BomAnalytics/v1.svc/compliance/substances | Get compliance for substances
*DocumentationApi* | [**get_miservicelayer_bom_analytics_v1svc_yaml**](docs/DocumentationApi.md#get_miservicelayer_bom_analytics_v1svc_yaml) | **GET** /BomAnalytics/v1.svc/yaml | Provides the YAML specification for this service
*ImpactedSubstancesApi* | [**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711**](docs/ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_bom1711) | **POST** /BomAnalytics/v1.svc/impacted-substances/bom1711 | Get the impacted substances for a BoM
*ImpactedSubstancesApi* | [**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials**](docs/ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_materials) | **POST** /BomAnalytics/v1.svc/impacted-substances/materials | Get the impacted substances for materials.
*ImpactedSubstancesApi* | [**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts**](docs/ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_parts) | **POST** /BomAnalytics/v1.svc/impacted-substances/parts | Get the impacted substances for parts
*ImpactedSubstancesApi* | [**post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications**](docs/ImpactedSubstancesApi.md#post_miservicelayer_bom_analytics_v1svc_impactedsubstances_specifications) | **POST** /BomAnalytics/v1.svc/impacted-substances/specifications | Get the impacted substances for specifications


## Models

 - [GrantaBomAnalyticsServicesInterfaceCommonCoatingWithCompliance](docs/GrantaBomAnalyticsServicesInterfaceCommonCoatingWithCompliance.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonImpactedSubstance](docs/GrantaBomAnalyticsServicesInterfaceCommonImpactedSubstance.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition](docs/GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonIndicatorResult](docs/GrantaBomAnalyticsServicesInterfaceCommonIndicatorResult.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances](docs/GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonMaterialReference](docs/GrantaBomAnalyticsServicesInterfaceCommonMaterialReference.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonMaterialWithCompliance](docs/GrantaBomAnalyticsServicesInterfaceCommonMaterialWithCompliance.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonPartReference](docs/GrantaBomAnalyticsServicesInterfaceCommonPartReference.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonPartWithCompliance](docs/GrantaBomAnalyticsServicesInterfaceCommonPartWithCompliance.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonRequestConfig](docs/GrantaBomAnalyticsServicesInterfaceCommonRequestConfig.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonSpecificationReference](docs/GrantaBomAnalyticsServicesInterfaceCommonSpecificationReference.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonSpecificationWithCompliance](docs/GrantaBomAnalyticsServicesInterfaceCommonSpecificationWithCompliance.md)
 - [GrantaBomAnalyticsServicesInterfaceCommonSubstanceWithCompliance](docs/GrantaBomAnalyticsServicesInterfaceCommonSubstanceWithCompliance.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Request](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Request.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Response](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForBom1711Response.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsResponse](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsRequest](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsResponse](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForPartsResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsRequest](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsResponse](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForSpecificationsResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesRequest](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesResponse](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesSubstanceWithAmount](docs/GrantaBomAnalyticsServicesInterfaceGetComplianceForSubstancesSubstanceWithAmount.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Request.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Response](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForBom1711Response.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsMaterial](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsMaterial.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsRequest](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForMaterialsResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsPart](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsPart.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsRequest](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsResponse](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForPartsResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsRequest](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsRequest.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse.md)
 - [GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsSpecification](docs/GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsSpecification.md)


## Author

