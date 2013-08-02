# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from museudigital.conteudos.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of museudigital.conteudos into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if museudigital.conteudos is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('museudigital.conteudos'))

    def test_uninstall(self):
        """Test if museudigital.conteudos is cleanly uninstalled."""
        self.installer.uninstallProducts(['museudigital.conteudos'])
        self.assertFalse(self.installer.isProductInstalled('museudigital.conteudos'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IMuseudigitalConteudosLayer is registered."""
        from museudigital.conteudos.interfaces import IMuseudigitalConteudosLayer
        from plone.browserlayer import utils
        self.failUnless(IMuseudigitalConteudosLayer in utils.registered_layers())
