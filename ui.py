import questionary
from typing import List
def ask_name():
    name = questionary.text('enter project name').ask()
    return name

def database(args : List[str]):
    database_name = questionary.select('what is your database' , choices=args , default='sqlite' , qmark='➽').ask()
    return database_name
