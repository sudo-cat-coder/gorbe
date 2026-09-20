import questionary
from typing import List
def ask_name():
    name = questionary.text('enter project name').ask()
    while not name:
        name = questionary.text('enter project name').ask()
    return name

def database(args : List[str]):
    database_name = questionary.select('what is your database' , choices=args , default='sqlite' , qmark='➽').ask()
    return database_name

def pip_or_uv():
    #pov short of pip or uv XD
    pov = questionary.select('which one?' , choices=['pip' , 'uv']) .ask()
    return pov
def docker():
    docker = questionary.confirm(('Do you want docker?')).ask()
    return docker

def framework():
    framework_name = questionary.select('wich framework do you want?',
                                        choices=[
                                        'Django&DRF',
                                        'FastAPI',
                                        'Flask'
                                        ]).ask()
    return framework_name
