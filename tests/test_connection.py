import dotenv as de
import os

import wiiki_editor.wiiki as wk

def test_connection():
    cwd = os.getcwd()
    secret_path = os.path.join(os.path.dirname(cwd), ".env")
    secrets = dict(de.dotenv_values(secret_path))
        
    wiiki = wk.Wiiki(secrets["USERNAME"], secrets["PASSWORD"], secrets["API"])

if __name__ == "__main__":
    os.system("pytest .")
