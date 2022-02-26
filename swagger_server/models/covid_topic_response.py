# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CovidTopicResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result: str=None):  # noqa: E501
        """CovidTopicResponse - a model defined in Swagger

        :param result: The result of this CovidTopicResponse.  # noqa: E501
        :type result: str
        """
        self.swagger_types = {
            'result': str
        }

        self.attribute_map = {
            'result': 'result'
        }
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'CovidTopicResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CovidTopicResponse of this CovidTopicResponse.  # noqa: E501
        :rtype: CovidTopicResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> str:
        """Gets the result of this CovidTopicResponse.


        :return: The result of this CovidTopicResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result: str):
        """Sets the result of this CovidTopicResponse.


        :param result: The result of this CovidTopicResponse.
        :type result: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result
