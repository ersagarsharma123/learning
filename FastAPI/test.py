from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
def main_page():
    return {"success": "welcome to 1st page"}

@app.get('/items/{item_id}')
def items(item_id:int):
    print('hloooooo')
    return {'success': f'{item_id} found in url'}

class ValidateData(BaseModel):
    print('1')
    int_value:int= Field(ge=0, description='+ve integer')
    string_value:str= Field(max_length=10, description='greter than 10')


@app.post('/submit/')
def submit(data:ValidateData):
    print('helo')
    try:
        return {'data':'success', 'int_value':data.int_value, 'string_value': data.string_value}
    except Exception as e:
        return {'failed': 'failed'}
