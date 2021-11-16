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


class GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances(Model):
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
        'legislation_name': 'str',
        'impacted_substances': 'list[GrantaBomAnalyticsServicesInterfaceCommonImpactedSubstance]'
    }

    attribute_map = {
        'legislation_name': 'LegislationName',
        'impacted_substances': 'ImpactedSubstances'
    }

    subtype_mapping = {
        
        'ImpactedSubstances': 'GrantaBomAnalyticsServicesInterfaceCommonImpactedSubstance'
    }


    def __init__(self, legislation_name=None, impacted_substances=None):  # noqa: E501
        """GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances - a model defined in Swagger"""  # noqa: E501
        self._legislation_name = None
        self._impacted_substances = None
        self.discriminator = None
        if legislation_name is not None:
            self.legislation_name = legislation_name
        if impacted_substances is not None:
            self.impacted_substances = impacted_substances

    @property
    def legislation_name(self):
        """Gets the legislation_name of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.  # noqa: E501


        :return: The legislation_name of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.  # noqa: E501
        :rtype: str
        """
        return self._legislation_name

    @legislation_name.setter
    def legislation_name(self, legislation_name):
        """Sets the legislation_name of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.


        :param legislation_name: The legislation_name of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.  # noqa: E501
        :type: str
        """

        self._legislation_name = legislation_name

    @property
    def impacted_substances(self):
        """Gets the impacted_substances of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.  # noqa: E501


        :return: The impacted_substances of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.  # noqa: E501
        :rtype: list[GrantaBomAnalyticsServicesInterfaceCommonImpactedSubstance]
        """
        return self._impacted_substances

    @impacted_substances.setter
    def impacted_substances(self, impacted_substances):
        """Sets the impacted_substances of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.


        :param impacted_substances: The impacted_substances of this GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances.  # noqa: E501
        :type: list[GrantaBomAnalyticsServicesInterfaceCommonImpactedSubstance]
        """

        self._impacted_substances = impacted_substances

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
        if issubclass(GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances, dict):
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
        if not isinstance(other, GrantaBomAnalyticsServicesInterfaceCommonLegislationWithImpactedSubstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
