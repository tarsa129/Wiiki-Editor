from unittest import TestCase

from src.wiiki_editor.wiiki_structures.wiiki_templates.misc_info_template import MiscInfoTemplate
from tests.wiiki_editor.wiiki_structures.wiiki_templates.template_test_helper_functions import read_template_from_file


class TestMiscInfoTemplateTemplate(TestCase):
    def test_set_arguments(self):
        template = MiscInfoTemplate(read_template_from_file("misc_info_test_basic_track.txt"))
        self.assertEqual(template.name, "{{PAGENAME}}")
