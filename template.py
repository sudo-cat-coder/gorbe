from typing import Dict

from jinja2 import Environment , FileSystemLoader
import os

def template_render(content : Dict):
    env = Environment(loader=FileSystemLoader(os.getcwd()) , trim_blocks=True , lstrip_blocks=True)
    template = env.get_template('templates/docker-compose.yaml.j2')

    output = template.render(**content)
    with open('docker-compose.yaml' , 'w') as f:
        f.write(output)
        return 'docker compose created'




#FASTAPI_MAIN =  "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\nasync def root():\n\treturn {'message' : 'Hello World!'}"


