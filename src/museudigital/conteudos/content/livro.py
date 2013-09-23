# -*- coding: utf-8 -*-

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata

from plone.app.folder.folder import ATFolder, ATFolderSchema

from museudigital.conteudos.config import PROJECTNAME
from museudigital.conteudos.interfaces import ILivro

LivroSchema = ATFolderSchema.copy()

schemata.finalizeATCTSchema(LivroSchema, folderish=True, moveDiscussion=False)


class Livro(ATFolder):
    """
    """

    implements(ILivro)

    meta_type = "Livro"
    schema = LivroSchema

    _at_rename_after_creation = True

atapi.registerType(Livro, PROJECTNAME)
