from typing import Dict

from jinja2 import Environment , FileSystemLoader
import os
from commands import get_templates_path

from jinja2.defaults import TRIM_BLOCKS

def docker_template(content : Dict , path : str , framework_name:str):
    env = Environment(loader=FileSystemLoader(get_templates_path()) , trim_blocks=True , lstrip_blocks=True)
    template = env.get_template('templates/docker-compose.yaml.j2')
    dockerfile_template = env.get_template('templates/dockerfile.j2')

    output = template.render(**content)
    dockerfile = dockerfile_template.render({'framework' : framework_name})
    with open(f'{path}/docker-compose.yaml' , 'w') as f:
        f.write(output)

    with open(f'{path}/Dockerfile' , 'w') as f:
        f.write(dockerfile)


def database_template(content : Dict , path:str , pov : str = 'pip' , name:str | None = None ) :
    env = Environment(loader=FileSystemLoader(get_templates_path()),trim_blocks=True , lstrip_blocks=True)
    template = env.get_template('/templates/database.py.j2')
    output = template.render(**content)
    if pov == 'uv':
        with open(f'{path}/src/database.py' , 'w') as f:
            f.write(output)
            return 'database file created with uv'

    with open(f'{path}/database.py' , 'w') as f:
        f.write(output)
        return 'database file created with pip'
#FASTAPI_MAIN =  "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\nasync def root():\n\treturn {'message' : 'Hello World!'}"


def fastapi_project(path:str | None = None ,name:str | None = None ,pov : str | None = None, content : Dict | None = None) -> None:
    env = Environment(loader=FileSystemLoader(get_templates_path()),trim_blocks=True , lstrip_blocks=True)
    template_main = env.get_template('/templates/main.py.j2')
    template_models = env.get_template('/templates/models.py.j2')
    template_router = env.get_template('/templates/router.py.j2')
    template_schema = env.get_template('/templates/schema.py.j2')

    
    output_main = template_main.render()
    output_models = template_models.render()
    output_router = template_router.render()
    output_schema = template_schema.render()
    if pov == 'uv':
        with open(f'{os.getcwd()}/{name}/{name}/src/main.py' ,'w')as f:
            f.write(output_main)

        with open(f'{os.getcwd()}/{name}/{name}/src/router.py' ,'w') as f:
            f.write(output_router)

        with open(f'{os.getcwd()}/{name}/{name}/src/schema.py' ,'w') as f:
            f.write(output_schema)
        
        with open(f'{os.getcwd()}/{name}/{name}/src/models.py' ,'w') as f:
            f.write(output_models)

    if pov == 'pip':
        with open(f'{path}/main.py', 'w') as f:
            f.write(output_main)
        with open(f'{path}/models.py', 'w') as f:
            f.write(output_models)
        with open(f'{path}/schema.py', 'w') as f:
            f.write(output_schema)
        with open(f'{path}/router.py', 'w') as f:
            f.write(output_router)



