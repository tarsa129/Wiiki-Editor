from __future__ import annotations

import copy as cp
import typing as tp

class DistributionSection(object):
    
    class Entry(object):
        
        def __init__(self, name: str, version: str = "", ct_id: str = "", dis_id: str = "") -> None:
            self.name = name
            self.version = version
            self.ct_id = ct_id
            self.dis_id = dis_id
            
            if name.startswith("A "):
                self.sort_attribute = name[2:].lower()
            elif name.startswith("The "):
                self.sort_attribute = name[4:].lower()
            elif name.startswith("s☆Ris"):
                self.sort_attribute = f"s{chr(ord('a') - 1)}ris CT Pack".lower()
            else:
                self.sort_attribute = name.lower()
        
        def __str__(self) -> str:
            if self.version:
                return f"* [[{self.name}]] ({self.version})"
            else:
                return f"* {{{{Distrib-ref|{self.name}|{self.ct_id}|{self.dis_id}}}}}"
        
        def __repr__(self) -> str:
            if self.version:
                return f"{self.name} ({self.version})"
            else:
                return f"{self.name} [{self.ct_id}|{self.dis_id}]"
    
    def __init__(self, text) -> None:
        end_of_header = text.find("[[distribution]]s:\n")
        if end_of_header == -1:
            raise ValueError("text is not properly formatted")
        
        self.header = text[:end_of_header + len("[[distribution]]s:\n")]
        text = text[end_of_header + len("[[distribution]]s:\n"):]
        
        begin_of_footer = text.rfind("\n\n")
        if begin_of_footer != -1:
            self.footer = text[begin_of_footer:]
            text = text[:begin_of_footer]
        else:
            self.footer = ""
        
        lines = text.split("\n")
        self.entries = []
        
        for line in lines:
            if line[2] == "{":
                _, name, ct_id, dis_id = line.strip("* {}").split("|")
                entry = DistributionSection.Entry(name, "", ct_id, dis_id)
            elif line[2] == "[":
                name, version = line.strip("* [)").split("]] (")
                entry = DistributionSection.Entry(name, version)
            else:
                continue
            self.entries.append(entry)
    
    def __str__(self) -> str:
        string = self.header
        string += "\n".join([str(entry) for entry in self.entries])
        string += self.footer
        return string
    
    def __repr__(self) -> str:
        return self.entries.__repr__()
    
    def __len__(self) -> int:
        return len(self.entries)
    
    def __add__(self, entry: tp.Self.Entry) -> tp.Self:
        if not isinstance(entry, DistributionSection.Entry):
            raise TypeError("unsupported type for entry: "
                            f"'{type(entry).__name__}'")
        
        result = cp.deepcopy(self)
        result.entries.append(entry)
        result.sort_entries()
        return result
    
    def __contains__(self, entry: tp.Self.Entry) -> bool:
        if not isinstance(entry, DistributionSection.Entry):
            raise TypeError("unsupported type for entry: "
                            f"'{type(entry).__name__}'")
        
        for e in self.entries:
            if e.name == entry.name:
                return True
        
        return False
    
    def sort_entries(self) -> None:
        self.entries = sorted(self.entries, key = lambda entry:entry.sort_attribute)
