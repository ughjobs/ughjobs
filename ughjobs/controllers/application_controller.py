import connexion
from ughjobs.models.application import Application
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def applications_get():
    """
    Wyświetlenie wszystkich zgłoszeń
    

    :rtype: None
    """
    return 'do some magic!'


def applications_id_delete(id):
    """
    Usunięcie zgłoszenia.
    
    :param id: Identyfikator zgłoszenia o prace
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def applications_id_get(id):
    """
    Wyświetlenie pojedynczego zgłoszenia
    
    :param id: Identyfikator zgłoszenia o prace
    :type id: int

    :rtype: Application
    """
    return 'do some magic!'


def jobs_id_apply_post(id, body=None):
    """
    Dodanie nowego zgłoszenia do oferty
    
    :param id: Identyfikator oferty pracy.
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Application.from_dict(connexion.request.get_json())
    return 'do some magic!'
