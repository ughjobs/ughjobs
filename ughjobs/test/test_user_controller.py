# coding: utf-8

from __future__ import absolute_import

from ughjobs.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUserController(BaseTestCase):
    """ UserController integration test stubs """

    def test_users_get(self):
        """
        Test case for users_get

        Wyświetlenie wszystkich użytkowników
        """
        response = self.client.open('/api/users',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_users_id_delete(self):
        """
        Test case for users_id_delete

        Usunięcie użytkownika.
        """
        response = self.client.open('/api/users/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_users_id_get(self):
        """
        Test case for users_id_get

        Wyświetlenie pojedynczego użytkownika
        """
        response = self.client.open('/api/users/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_users_post(self):
        """
        Test case for users_post

        Dodanie nowego użytkownika
        """
        body = User()
        response = self.client.open('/api/users',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
