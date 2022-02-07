# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CovidTopicRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, target_id: int=None, text: str=None):  # noqa: E501
        """CovidTopicRequest - a model defined in Swagger

        :param target_id: The target_id of this CovidTopicRequest.  # noqa: E501
        :type target_id: int
        :param text: The text of this CovidTopicRequest.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'target_id': int,
            'text': str
        }

        self.attribute_map = {
            'target_id': 'targetId',
            'text': 'text'
        }

        self._target_id = target_id
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'CovidTopicRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CovidTopicRequest of this CovidTopicRequest.  # noqa: E501
        :rtype: CovidTopicRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_id(self) -> int:
        """Gets the target_id of this CovidTopicRequest.


        :return: The target_id of this CovidTopicRequest.
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id: int):
        """Sets the target_id of this CovidTopicRequest.


        :param target_id: The target_id of this CovidTopicRequest.
        :type target_id: int
        """
        if target_id is None:
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501

        self._target_id = target_id

    @property
    def text(self) -> str:
        """Gets the text of this CovidTopicRequest.


        :return: The text of this CovidTopicRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this CovidTopicRequest.


        :param text: The text of this CovidTopicRequest.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text
