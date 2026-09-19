FASTAPI_MAIN =  "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\nasync def root():\n\treturn {'message' : 'Hello World!'}"
