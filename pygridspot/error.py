"""
    ============================================
    :mod:`error` -- Gridspot Exception class
    ============================================

    .. Copyright 2012 Amir Elaguizy 

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.
       
    .. module:: error
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
""" 

class GridspotError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

