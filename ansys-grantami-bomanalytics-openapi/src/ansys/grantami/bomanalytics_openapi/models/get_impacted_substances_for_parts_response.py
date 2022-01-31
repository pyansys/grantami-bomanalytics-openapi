# coding: utf-8

"""
    Granta.BomAnalyticsServices

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import ModelBase


class GetImpactedSubstancesForPartsResponse(ModelBase):
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
        'parts': 'list[GetImpactedSubstancesForPartsPart]',
        'log_messages': 'list[CommonLogEntry]'
    }

    attribute_map = {
        'parts': 'Parts',
        'log_messages': 'LogMessages'
    }

    subtype_mapping = {
        'Parts': 'GetImpactedSubstancesForPartsPart',
        'LogMessages': 'CommonLogEntry'
    }


    def __init__(self, parts=None, log_messages=None):  # noqa: E501
        """GetImpactedSubstancesForPartsResponse - a model defined in Swagger"""  # noqa: E501
        self._parts = None
        self._log_messages = None
        self.discriminator = None
        if parts is not None:
            self.parts = parts
        if log_messages is not None:
            self.log_messages = log_messages

    @property
    def parts(self):
        """Gets the parts of this GetImpactedSubstancesForPartsResponse.  # noqa: E501

        :return: The parts of this GetImpactedSubstancesForPartsResponse.  # noqa: E501
        :rtype: list[GetImpactedSubstancesForPartsPart]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this GetImpactedSubstancesForPartsResponse.

        :param parts: The parts of this GetImpactedSubstancesForPartsResponse.  # noqa: E501
        :type: list[GetImpactedSubstancesForPartsPart]
        """
        self._parts = parts

    @property
    def log_messages(self):
        """Gets the log_messages of this GetImpactedSubstancesForPartsResponse.  # noqa: E501

        :return: The log_messages of this GetImpactedSubstancesForPartsResponse.  # noqa: E501
        :rtype: list[CommonLogEntry]
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages):
        """Sets the log_messages of this GetImpactedSubstancesForPartsResponse.

        :param log_messages: The log_messages of this GetImpactedSubstancesForPartsResponse.  # noqa: E501
        :type: list[CommonLogEntry]
        """
        self._log_messages = log_messages

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
        if issubclass(GetImpactedSubstancesForPartsResponse, dict):
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
        if not isinstance(other, GetImpactedSubstancesForPartsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
