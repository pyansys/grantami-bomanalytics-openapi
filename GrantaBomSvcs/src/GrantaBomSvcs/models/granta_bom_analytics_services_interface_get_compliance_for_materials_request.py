# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import Model


class GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'materials': 'list[GrantaBomAnalyticsServicesInterfaceCommonMaterialReference]',
        'indicators': 'list[GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition]',
        'database_key': 'str',
        'config': 'GrantaBomAnalyticsServicesInterfaceCommonRequestConfig'
    }

    attribute_map = {
        'materials': 'Materials',
        'indicators': 'Indicators',
        'database_key': 'DatabaseKey',
        'config': 'Config'
    }

    subtype_mapping = {
        'Materials': 'GrantaBomAnalyticsServicesInterfaceCommonMaterialReference',
        'Indicators': 'GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition',
        'Config': 'GrantaBomAnalyticsServicesInterfaceCommonRequestConfig'
    }


    def __init__(self, materials=None, indicators=None, database_key=None, config=None):  # noqa: E501
        """GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest - a model defined in Swagger"""  # noqa: E501
        self._materials = None
        self._indicators = None
        self._database_key = None
        self._config = None
        self.discriminator = None
        if materials is not None:
            self.materials = materials
        if indicators is not None:
            self.indicators = indicators
        if database_key is not None:
            self.database_key = database_key
        if config is not None:
            self.config = config

    @property
    def materials(self):
        """Gets the materials of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501

        :return: The materials of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :rtype: list[GrantaBomAnalyticsServicesInterfaceCommonMaterialReference]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.

        :param materials: The materials of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :type: list[GrantaBomAnalyticsServicesInterfaceCommonMaterialReference]
        """
        self._materials = materials

    @property
    def indicators(self):
        """Gets the indicators of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501

        :return: The indicators of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :rtype: list[GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.

        :param indicators: The indicators of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :type: list[GrantaBomAnalyticsServicesInterfaceCommonIndicatorDefinition]
        """
        self._indicators = indicators

    @property
    def database_key(self):
        """Gets the database_key of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501

        :return: The database_key of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.

        :param database_key: The database_key of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    @property
    def config(self):
        """Gets the config of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501

        :return: The config of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :rtype: GrantaBomAnalyticsServicesInterfaceCommonRequestConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.

        :param config: The config of this GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest.  # noqa: E501
        :type: GrantaBomAnalyticsServicesInterfaceCommonRequestConfig
        """
        self._config = config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaBomAnalyticsServicesInterfaceGetComplianceForMaterialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other