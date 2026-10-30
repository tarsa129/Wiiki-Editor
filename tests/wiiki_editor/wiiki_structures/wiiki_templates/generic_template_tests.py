from unittest import TestCase

import wikitextparser

from src.wiiki_editor.wiiki_structures.wiiki_templates.generic_template import WiikiTemplate

# these tests are not particularly useful because the generic template does not accept any arguments. 
class TestGenericWiikiTemplate(TestCase):
    def setUp(self):
        self.template = WiikiTemplate(wikitextparser.parse("{{obj-ref|0x129|tarsa129}}").templates[0])

    def tearDown(self):
        del self.template

    def test_get_arguments(self):
        self.assertDictEqual(self.template._get_arguments(), {})

    def test_to_text(self):
        self.assertEqual(str(self.template), "{{obj-ref}}")
