from fastapi import FastAPI
import unicorn
from pydantic import BaseModel

app = FastAPI()

@app.get('/first_blood')
def test_func():
  return 'Hello Test'

if __name__ == '__main__':
  unicorn.run('first_blood:app', host='127.0.0.1', port=4557, reload=True)