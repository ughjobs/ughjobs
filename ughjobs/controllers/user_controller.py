import connexion
from ughjobs.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def users_get():
    """
    Wyświetlenie wszystkich użytkowników
    

    :rtype: None
    """
    return 'do some magic!'


def users_id_delete(id):
    """
    Usunięcie użytkownika.
    
    :param id: Identyfikator użytkownika.
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def users_id_get(id):
    """
    Wyświetlenie pojedynczego użytkownika
    
    :param id: Identyfikator użytkownika.
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def users_post(body=None):
    """
    Dodanie nowego użytkownika
    
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())
    return 'do some magic!'
