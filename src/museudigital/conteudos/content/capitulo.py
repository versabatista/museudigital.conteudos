# -*- coding: utf-8 -*-

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.newsitem import ATNewsItem, ATNewsItemSchema

from museudigital.conteudos.config import PROJECTNAME
from museudigital.conteudos.interfaces import ICapitulo

CapituloSchema = ATNewsItemSchema.copy()

schemata.finalizeATCTSchema(CapituloSchema, folderish=True, moveDiscussion=False)


class Capitulo(ATNewsItem):
    """
    """

    implements(ICapitulo)

    meta_type = "Capitulo"
    schema = CapituloSchema

    _at_rename_after_creation = True

atapi.registerType(Capitulo, PROJECTNAME)
