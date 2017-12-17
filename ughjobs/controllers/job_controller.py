import connexion
from ughjobs.models.job import Job
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def jobs_get():
    """
    Wyświetlenie wszystkich ofert pracy
    

    :rtype: None
    """
    return 'do some magic!'


def jobs_id_delete(id):
    """
    Usunięcie oferty.
    
    :param id: Identyfikator oferty pracy.
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def jobs_id_get(id):
    """
    Wyświetlenie pojedynczej oferty
    
    :param id: Identyfikator oferty pracy.
    :type id: int

    :rtype: Job
    """
    return 'do some magic!'


def jobs_post(body=None):
    """
    Dodanie nowego ogłoszenia
    
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Job.from_dict(connexion.request.get_json())
    return 'do some magic!'
