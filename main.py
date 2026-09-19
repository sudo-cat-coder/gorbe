from template import FASTAPI_MAIN
from ui import ask_name , database
from fs import create_folder
name = ask_name()
print(name)
try:
    create_folder(name)
except Exception as error:
    print(error)
db_name = database(['mongoDB' ,'mysql', 'sqlite' , 'postgresql'])
if db_name == 'sqlite':
    print('good choice')
print(db_name)
