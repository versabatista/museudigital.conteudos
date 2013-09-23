# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from museudigital.conteudos.testing import INTEGRATION_TESTING
from museudigital.conteudos.interfaces import IAcervo
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestAcervo(unittest.TestCase):
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
        self.folder.invokeFactory('Acervo', 'acervo')
        a1 = self.folder['acervo']
        self.failUnless(IAcervo.providedBy(a1))

    def test_factorytool(self):
        ft = getToolByName(self.portal, 'portal_factory')
        ids = ft.getFactoryTypes().keys()
        self.assertTrue('Acervo' in ids)
