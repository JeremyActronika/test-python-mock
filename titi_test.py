from titi import Titi
import mock
import unittest
import pycodestyle


class TestTiti(unittest.TestCase):
    def setUp(self):
        self.titi = Titi()

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['titi.py', 'titi_test.py'])
        self.assertEqual(
                result.total_errors,
                0,
                "Found code tyle errors (and warnings)."
            )

    def test_name(self):
        self.assertEqual(self.titi.name, "titi")
        self.assertEqual(self.titi, self.titi.setName("toto"))
        self.assertEqual(self.titi.name, "toto")

    def test_toto(self):
        self.titi.toto = mock.Mock(name='toto')
        self.titi.toto.value = "Caribou"
        self.assertEqual(self.titi.getTotoValue(), "Caribou")
