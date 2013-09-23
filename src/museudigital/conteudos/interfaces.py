# -*- coding: utf-8 -*-

from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IMuseudigitalConteudosLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IAcervo(Interface):
    """ Marker interface for content
    """


class ICapitulo(Interface):
    """ Marker interface for content
    """


class ILivro(Interface):
    """ Marker interface for content
    """
