import dotenv as de
import os

import wiiki_editor.wiiki as wk
import wiiki_editor.article as wa

cwd = os.getcwd()
secret_path = os.path.join(os.path.dirname(cwd), ".env")
secrets = dict(de.dotenv_values(secret_path))
    
wiiki = wk.Wiiki(secrets["USERNAME"], secrets["PASSWORD"], secrets["API"])

article = wa.Article("Chain Chomp Rollercoaster (Mario Circuit Edit)", wiiki)
