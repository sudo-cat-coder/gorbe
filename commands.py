import os
import subprocess
from typing import List
import rich
from rich.console import Console

def install_packeage(name):
    os.system(f'uv add {name}')
    os.system(f'uv pip install {name}')
    return

def uv_inital(path : str , name:str, packages : List[str]):
    
    console = Console()
    os.system(f'uv init {path}/{name} > /dev/null 2>&1 ')
    #os.system(f' cd {os.getcwd()}/{name}/{name} ; uv add {package} > /dev/null 2>&1')
    with console.status("[bold green]Installing packages...[/bold green]",
                        spinner="dots"):

        for package in packages :

            os.system(f' cd {os.getcwd()}/{name}/{name} && uv add {package}> /dev/null 2>&1' )
    return 'created'

def venv(path):
    subprocess.run(['python' , '-m' , 'venv' , '.venv'],check=True , cwd=path)
    return   

def install_package_pip(names: List[str], path: str):
    console = Console()
    venv_path = f"{path}/.venv/bin/python"

    with console.status(
        "[bold green]Installing packages...[/bold green]",
        spinner="dots"
    ):
        for name in names:
            result = subprocess.run(
                [venv_path, "-m", "pip", "install", name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if result.returncode != 0:
                return False
    return True

def django_start(name: str , path:str | None = None):
    os.system(f'cd {os.getcwd()}/{name}/{name}/src && uv run django-admin startproject {name}_django .')
    #print(f'cd {os.getcwd()}/{name}/src && uv run django-admin startproject {name} .')
    return


def git_init(path:str):
    os.system(f'cd {path} && git init > /dev/null 2>&1 ')
    return

import sys
import os

def get_templates_path():
    if getattr(sys, 'frozen', False):
        # حالت اجرای فایل اجرایی PyInstaller
        base = sys._MEIPASS
    else:
        # حالت اجرای عادی از سورس
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "templates")
