from template import FASTAPI_MAIN
from ui import ask_name , database , pip_or_uv
from fs import create_folder
from commands import inital


name = ask_name()
print(name)
try:
    folder = create_folder(name)
    init = inital(path=folder , name=name)

except Exception as error:
    print(error)

db_name = database(['mongoDB' ,'mysql', 'sqlite' , 'postgresql'])
if db_name == 'sqlite':
    print('good choice')
print(db_name)
pov = pip_or_uv()
print(pov)
