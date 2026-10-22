from wikitextparser import Template


class WiikiTemplate:
    ordered_arguments = []
    all_arguments = set(ordered_arguments)

    def __init__(self, mediawiki_template: Template):
        self.mediawiki_template = mediawiki_template

        for arg in self.mediawiki_template.arguments:
            self.mediawiki_template.set_arg(arg.name, arg.value.strip())

        self.arguments = {argument.name: argument.value for argument in self.mediawiki_template.arguments}

    # get and set arguments is a common operation, so use a hash-based lookup
    # as opposed to list-based wtp arguments list.
    def get_arguments(self) -> dict[str, str]:
        return self.arguments

    def get_argument(self, arg: str) -> str:
        return self.arguments[arg] if arg in self.arguments else None

    # avoid checking the list of allowed arguments, as they are taken out when
    def set_argument(self, argument: str, value: str):
        if argument in self.__class__.all_arguments:
            self.arguments[argument] = value.strip()

    # when doing one operation on one page, to_text only needs to be called once (when saving back)
    def to_text(self, single_line=False):
        self._reorder_args()
        return str(self) if single_line else self.mediawiki_template.pformat()

    def _reorder_args(self, single_line=False):
        for arg in reversed(self.mediawiki_template.arguments):
            del arg[:]
        for argument in self.__class__.ordered_arguments:
            if argument in self.arguments:
                if single_line:
                    self.mediawiki_template.set_arg(argument, self.arguments[argument])
                else:
                    self.mediawiki_template.set_arg(argument, f" {self.arguments[argument]}")
