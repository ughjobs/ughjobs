# coding: utf-8

from __future__ import absolute_import

from ughjobs.models.job import Job
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestJobController(BaseTestCase):
    """ JobController integration test stubs """

    def test_jobs_get(self):
        """
        Test case for jobs_get

        Wyświetlenie wszystkich ofert pracy
        """
        response = self.client.open('/api/jobs',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_jobs_id_delete(self):
        """
        Test case for jobs_id_delete

        Usunięcie oferty.
        """
        response = self.client.open('/api/jobs/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_jobs_id_get(self):
        """
        Test case for jobs_id_get

        Wyświetlenie pojedynczej oferty
        """
        response = self.client.open('/api/jobs/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_jobs_post(self):
        """
        Test case for jobs_post

        Dodanie nowego ogłoszenia
        """
        body = Job()
        response = self.client.open('/api/jobs',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
