# -*- coding: utf-8 -*-

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.newsitem import ATNewsItem, ATNewsItemSchema

from museudigital.conteudos.config import PROJECTNAME
from museudigital.conteudos.interfaces import IAcervo

AcervoSchema = ATNewsItemSchema.copy()

schemata.finalizeATCTSchema(AcervoSchema, folderish=True, moveDiscussion=False)


class Acervo(ATNewsItem):
    """
    """

    implements(IAcervo)

    meta_type = "Acervo"
    schema = AcervoSchema

    _at_rename_after_creation = True

atapi.registerType(Acervo, PROJECTNAME)
