# coding: utf-8

from __future__ import absolute_import
#from ughjobs.models.byte_array import ByteArray
import re
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Job(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, company=None, expire=None, content=None):
        """
        Job - a model defined in Swagger

        :param id: The id of this Job.
        :type id: int
        :param company: The company of this Job.
        :type company: int
        :param expire: The expire of this Job.
        :type expire: date
        :param content: The content of this Job.
        :type content: ByteArray
        """
        self.swagger_types = {
            'id': int,
            'company': int,
            'expire': date,
            'content': bytearray
        }

        self.attribute_map = {
            'id': 'id',
            'company': 'company',
            'expire': 'expire',
            'content': 'content'
        }

        self._id = id
        self._company = company
        self._expire = expire
        self._content = content

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Job of this Job.
        :rtype: Job
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self):
        """
        Gets the id of this Job.

        :return: The id of this Job.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Job.

        :param id: The id of this Job.
        :type id: int
        """

        self._id = id

    @property
    def company(self):
        """
        Gets the company of this Job.

        :return: The company of this Job.
        :rtype: int
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Job.

        :param company: The company of this Job.
        :type company: int
        """

        self._company = company

    @property
    def expire(self):
        """
        Gets the expire of this Job.

        :return: The expire of this Job.
        :rtype: date
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """
        Sets the expire of this Job.

        :param expire: The expire of this Job.
        :type expire: date
        """

        self._expire = expire

    @property
    def content(self):
        """
        Gets the content of this Job.

        :return: The content of this Job.
        :rtype: ByteArray
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Job.

        :param content: The content of this Job.
        :type content: ByteArray
        """
        if content is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', content):
            raise ValueError("Invalid value for `content`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self._content = content

