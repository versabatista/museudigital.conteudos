# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from museudigital.conteudos.testing import INTEGRATION_TESTING
from museudigital.conteudos.interfaces import ICapitulo
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestCapitulo(unittest.TestCase):
    """Test content type."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        # first, add a Livro content type
        self.folder.invokeFactory('Livro', 'livro')
        livro = self.folder['livro']
        livro.invokeFactory('Capitulo', 'capitulo')
        a1 = livro['capitulo']
        self.failUnless(ICapitulo.providedBy(a1))

    def test_factorytool(self):
        ft = getToolByName(self.portal, 'portal_factory')
        ids = ft.getFactoryTypes().keys()
        self.assertTrue('Capitulo' in ids)
