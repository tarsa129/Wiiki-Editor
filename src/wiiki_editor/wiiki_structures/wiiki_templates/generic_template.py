from wikitextparser import Template


class WiikiTemplate:
    named = False

    def __init__(self, mediawiki_template: Template):
        self.mediawiki_template = mediawiki_template

        # we always want to strip unnecessary whitespace from arguments
        for arg in self.mediawiki_template.arguments:
            self.mediawiki_template.set_arg(arg.name, arg.value.strip())
        self._set_arguments(mediawiki_template)

    def _set_arguments(self, mediawiki_template: Template):
        # here, the template arguments are converted to instance variables
        # this logic is left to each class
        pass

    # when doing one operation on one page, to_text only needs to be called once (when saving back)
    def to_text(self):
        self._assign_arguments(self._get_arguments())
        if self.__class__.named:
            return self.mediawiki_template.pformat(indent='').replace(r"\n[|] (.*) = (.*)", r"\n|\1= \2")
        else:
            return str(self.mediawiki_template)

    def _get_arguments(self):
        # here, the instance variables are converted to a dict.
        # this logic is left to each class
        return {}

    def _assign_arguments(self, arguments):
        for arg in reversed(self.mediawiki_template.arguments):
            del arg[:]
        for name, value in arguments.items():
            self.mediawiki_template.set_arg(name, value)
