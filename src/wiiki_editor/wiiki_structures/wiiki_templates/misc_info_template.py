from wikitextparser import Template

from src.wiiki_editor.wiiki_structures.wiiki_templates.generic_template import WiikiTemplate


class MiscInfoTemplateImage:
    def __init__(self, file=None, wbz_id=None, description=None):
        self.file = file
        self.wbz_id = wbz_id
        self.description = description

    def __bool__(self):
        return bool(self.file) or bool(self.wbz_id) or bool(self.description)


class MiscInfoTemplate(WiikiTemplate):

    def __init__(self, mediawiki: Template):
        super().__init__(mediawiki)

    def _set_arguments(self, mediawiki_template: Template):
        self.name = mediawiki_template.get_arg_value_or_default("name")
        self.wbz_id = mediawiki_template.get_arg_value_or_default("wbz-id")

        self.images = []
        self.images.append(MiscInfoTemplateImage(mediawiki_template.get_arg_value_or_default("image"),
                                      mediawiki_template.get_arg_value_or_default("image-id"),
                                      mediawiki_template.get_arg_value_or_default("image-description")))
        for i in range(2, 11):
            self.images.append(MiscInfoTemplateImage(mediawiki_template.get_arg_value_or_default(f"image{i}"),
                                          mediawiki_template.get_arg_value_or_default(f"image-id{i}"),
                                          mediawiki_template.get_arg_value_or_default(f"image-description{i}")))
        self.images = list(filter(lambda x: bool(x), self.images))

        self.author = mediawiki_template.get_arg_value_or_default("author")
        self.creator = mediawiki_template.get_arg_value_or_default("creator")
        self.designer = mediawiki_template.get_arg_value_or_default("designer")

        self.version = mediawiki_template.get_arg_value_or_default("version")
        self.date_of_release = mediawiki_template.get_arg_value_or_default("date of release")
        self.editors_used = mediawiki_template.get_arg_value_or_default("editors used")
        self.scale = mediawiki_template.get_arg_value_or_default("scale")
        self.ai_usage = mediawiki_template.get_arg_value_or_default("ai usage")

        self.downloads = []
        self.downloads.append(mediawiki_template.get_arg_value_or_default("download"))
        for i in range(2, 11):
            self.downloads.append(mediawiki_template.get_arg_value_or_default(f"download{i}"))
        self.downloads = list(filter(lambda x: x is not None, self.downloads))