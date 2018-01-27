# coding: utf-8

from __future__ import absolute_import

from ughjobs.models.application import Application
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestApplicationController(BaseTestCase):
    """ ApplicationController integration test stubs """

    def test_applications_get(self):
        """
        Test case for applications_get

        Wyświetlenie wszystkich zgłoszeń
        """
        response = self.client.open('/api/applications',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_applications_id_delete(self):
        """
        Test case for applications_id_delete

        Usunięcie zgłoszenia.
        """
        response = self.client.open('/api/applications/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_applications_id_get(self):
        """
        Test case for applications_id_get

        Wyświetlenie pojedynczego zgłoszenia
        """
        response = self.client.open('/api/applications/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_jobs_id_apply_post(self):
        """
        Test case for jobs_id_apply_post

        Dodanie nowego zgłoszenia do oferty
        """
        body = Application()
        response = self.client.open('/api/jobs/{id}/apply'.format(id=56),
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
