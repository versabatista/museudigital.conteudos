# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from museudigital.conteudos.testing import INTEGRATION_TESTING
from museudigital.conteudos.interfaces import ILivro
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestLivro(unittest.TestCase):
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
        self.folder.invokeFactory('Livro', 'livro')
        a1 = self.folder['livro']
        self.failUnless(ILivro.providedBy(a1))

    def test_factorytool(self):
        ft = getToolByName(self.portal, 'portal_factory')
        ids = ft.getFactoryTypes().keys()
        self.assertTrue('Livro' in ids)
