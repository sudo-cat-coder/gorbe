import questionary
from typing import List
import rich
from rich.console import Console
from rich.panel import Panel


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
                                        'Django',
                                        'FastAPI',
                                        'Flask'
                                        ]).ask()
    return framework_name

def wanrning(path:str):
    console = Console()

    console.print(
    Panel(
        "Virtual environment not activate .\n"
        f"Run `source {path}/.venv/bin/activate` to activate it.",
        title="⚠ Warning",
        border_style="red"
        )
    )




def user_perfrence_for_database(db_name : str) -> dict:
    content = {}
    content['DB']=questionary.text('what is DB name?' , default='db' ).ask()
    content['USER']=questionary.text('what is DB user name?' , default='root').ask()
    content['PASSWORD']=questionary.text('what is DB password?' , default='123').ask()
    if db_name == 'mysql':
        content['ROOT_PASSWORD'] = questionary.text('what is your root password' , default='123').ask()
    return content

def api_key():
    questionary.text('enter your apki key : ').ask()
