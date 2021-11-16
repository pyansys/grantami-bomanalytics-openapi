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


class GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse(Model):
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
        'specifications': 'list[GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsSpecification]'
    }

    attribute_map = {
        'specifications': 'Specifications'
    }

    subtype_mapping = {
        'Specifications': 'GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsSpecification'
    }


    def __init__(self, specifications=None):  # noqa: E501
        """GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse - a model defined in Swagger"""  # noqa: E501
        self._specifications = None
        self.discriminator = None
        if specifications is not None:
            self.specifications = specifications

    @property
    def specifications(self):
        """Gets the specifications of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse.  # noqa: E501


        :return: The specifications of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse.  # noqa: E501
        :rtype: list[GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsSpecification]
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse.


        :param specifications: The specifications of this GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse.  # noqa: E501
        :type: list[GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsSpecification]
        """

        self._specifications = specifications

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
        if issubclass(GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse, dict):
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
        if not isinstance(other, GrantaBomAnalyticsServicesInterfaceGetImpactedSubstancesForSpecificationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
