from __future__ import annotations
import mwclient as mc

from . import article as ac

class Wiiki(object):
    
    def __init__(self, username: str, password: str, api: str) -> None:
        if not isinstance(username, str):
            raise TypeError("unsupported type for username: "
                            f"'{type(username).__name__}'")
        
        if not isinstance(password, str):
            raise TypeError("unsupported type for password: "
                            f"'{type(password).__name__}'")
        
        if not isinstance(api, str):
            raise TypeError("unsupported type for api: "
                            f"'{type(api).__name__}'")
        
        session = mc.Site("wiki.tockdom.com", custom_headers = {"User-Agent": api})
        session.login(username, password)
        self.session = session
        self.username = username
    
    def __repr__(self) -> str:
        return f"{self.username} on Custom Mario Kart Wiiki"
    
    def article(self, title: str | int) -> ac.Article:
        return ac.Article(title, self)
    
    def search(self, query, where = "title", namespace = 0):
        l = []
        for article in self.session.search(query, namespace, where):
            l.append(article.get("title"))
        if not bool(l):
            return None
        elif len(l) == 1:
            return l[0]
        else:
            return l
    
    def edit(self, title, text, summary = "", minor = False):
        page = ac.Article(title, self.session)
        page.object.edit(text, summary, minor)
    
    def move(self, title, new_title, summary = "", redirect = False):
        page = ac.Article(title, self.session)
        page.object.move(new_title, reason = summary, no_redirect = not redirect)
    
    def articles_in_category(self, name):
        category = self.session.categories[name]
        names = set()
        for article in category:
            names.add(article.name)
        return names
