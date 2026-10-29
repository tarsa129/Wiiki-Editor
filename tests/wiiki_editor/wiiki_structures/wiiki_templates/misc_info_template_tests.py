from unittest import TestCase

from src.wiiki_editor.wiiki_structures.wiiki_templates.misc_info_template import MiscInfoTemplate
from tests.wiiki_editor.wiiki_structures.wiiki_templates.template_test_helper_functions import read_template_from_file


class TestMiscInfoTemplateTemplate(TestCase):
    def test_basic_track(self):
        template = MiscInfoTemplate(read_template_from_file("misc_info_test_basic_track.txt"))
        self.assertEqual(template.name, "{{PAGENAME}}")
        self.assertEqual(len(template.images), 1)
        self.assertEqual(template.images[0].wbz_id, "20703")
        self.assertEqual(template.version, "v2.0")
        self.assertEqual(template.date_of_release, "2024-05-07")
        self.assertEqual(template.wbz_id, "11621")
        self.assertListEqual(template.downloads, ["https://drive.google.com/file/d/1tzJ6rg9RZ98jK_v5bYVT_rnIV51iKNsY"])

        self.assertIsNone(template.scale)
        self.assertIsNone(template.ai_usage)

    def test_fix_lists(self):
        template = MiscInfoTemplate(read_template_from_file("misc_info_test_fix_lists.txt"))
        self.assertEqual(template.name, "{{PAGENAME}}")
        self.assertEqual(len(template.images), 1)
        self.assertEqual(template.images[0].wbz_id, "20703")
        self.assertEqual(template.version, "v2.0")
        self.assertEqual(template.date_of_release, "2024-05-07")
        self.assertEqual(template.wbz_id, "11621")
        self.assertListEqual(template.downloads, ["https://drive.google.com/file/d/1tzJ6rg9RZ98jK_v5bYVT_rnIV51iKNsY"])

        self.assertIsNone(template.scale)
        self.assertIsNone(template.ai_usage)