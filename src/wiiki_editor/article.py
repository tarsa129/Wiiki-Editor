from __future__ import annotations
import mwclient as mc

from . import wiiki as wk

class Article(object):
    
    def __init__(self, title: str | int, wiiki: wk.Wiiki) -> None:
        if not isinstance(title, str | int):
            raise TypeError("unsupported type for title: "
                            f"'{type(title).__name__}'")
        
        if not isinstance(wiiki, wk.Wiiki):
            raise TypeError("unsupported type for wiiki: "
                            f"'{type(wiiki).__name__}'")
        
        self.session = wiiki.session
        self.object = mc.page.Page(wiiki.session, title)
        self.title = self.object.name
    
    def __repr__(self) -> str:
        return f"Article {self.title} on Custom Mario Kart Wiiki"
    
    def get_text(self, section = -1) -> str:
        if section == -1:
            return self.object.text()
        else:
            return self.object.text(section)
    
    def edit_text(self, text: str, summary = "", section = -1, minor = False) -> None:
        if section == -1:
            self.object.edit(text, summary, minor)
        else:
            self.object.edit(text, summary, minor, section = section)
    
    def categories(self) -> list[str]:
        categories = set()
        for category in self.object.categories():
            categories.add(category.name)
        return categories
