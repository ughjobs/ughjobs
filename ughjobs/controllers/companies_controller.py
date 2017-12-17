import connexion
from ughjobs.models.company import Company
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def companies_get():
    """
    Wyświetlenie wszystkich firm
    

    :rtype: None
    """
    return 'do some magic!'


def companies_id_delete(id):
    """
    Usunięcie firmy.
    
    :param id: Identyfikator firmy
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def companies_id_get(id):
    """
    Wyświetlenie pojedynczej firmy
    
    :param id: Identyfikator firmy
    :type id: int

    :rtype: Company
    """
    return 'do some magic!'


def companies_post(body=None):
    """
    Dodanie nowej firmy
    
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())
    return 'do some magic!'
