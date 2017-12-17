# coding: utf-8

from __future__ import absolute_import

from ughjobs.models.company import Company
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCompaniesController(BaseTestCase):
    """ CompaniesController integration test stubs """

    def test_companies_get(self):
        """
        Test case for companies_get

        Wyświetlenie wszystkich firm
        """
        response = self.client.open('/api/companies',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_companies_id_delete(self):
        """
        Test case for companies_id_delete

        Usunięcie firmy.
        """
        response = self.client.open('/api/companies/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_companies_id_get(self):
        """
        Test case for companies_id_get

        Wyświetlenie pojedynczej firmy
        """
        response = self.client.open('/api/companies/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_companies_post(self):
        """
        Test case for companies_post

        Dodanie nowej firmy
        """
        body = Company()
        response = self.client.open('/api/companies',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
