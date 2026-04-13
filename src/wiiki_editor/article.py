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
    
    def get_sections(self) -> list[str]:
        texts = []
        i = 0
        # Try sections 0, 1, 2, ... until there exist no more
        while True:
            try:
                texts.append(self.get_text(i))
                i += 1
            except KeyError:
                break
        
        # Get every title of every section and store them
        sections = []
        for j, text in enumerate(texts):
            header = text.split("\n")[0]
            
            # Handle the first "header" separately
            if j == 0 and not header.startswith("="):
                sections.append("0")
                continue
            
            title = header.strip("=").strip()
            sections.append(title)
        
        return sections
    
    def get_text(self, section: int | str = -1) -> str:
        if section == -1:
            return self.object.text()
        elif isinstance(section, int):
            return self.object.text(section)
        else:
            sections = self.get_sections()
            if section not in sections:
                raise KeyError(f"section '{section}' is not present in article")
            
            return self.get_text(sections.index(section))
    
    def edit_text(self, text: str, summary: str = "", section: int | str = -1, minor: bool = False) -> None:
        if section == -1:
            self.object.edit(text, summary, minor)
        elif isinstance(section, int):
            self.object.edit(text, summary, minor, section = section)
        else:
            sections = self.get_sections()
            if section not in sections:
                raise KeyError(f"section '{section}' is not present in article")
            
            return self.edit_text(text, summary, sections.index(section), minor)
    
    def categories(self) -> list[str]:
        categories = set()
        for category in self.object.categories():
            categories.add(category.name)
        return categories
