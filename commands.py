import os
import subprocess
import rich
from rich.console import Console
def install_packeage(name):
    os.system(f'uv add {name}')
    os.system(f'uv pip install {name}')
    return

def inital(path : str , name:str):
    
    os.system(f'uv init {path}/{name} > /dev/null 2>&1 ')
    return 'created'

def venv(path):
    subprocess.run(['python' , '-m' , 'venv' , '.venv'],check=True , cwd=path)
    return   

def install_package_pip(name: str, path: str):
    console = Console()
    venv_path = f"{path}/.venv/bin/python"

    with console.status(
        "[bold green]Installing packages...[/bold green]",
        spinner="dots"
    ):
        result = subprocess.run(
            [venv_path, "-m", "pip", "install", name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    return result.returncode == 0
