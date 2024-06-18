from fastapi import FastAPI
import unicorn
from pydantic import BaseModel

app = FastAPI()



if __name__ == '__main__':
  unicorn.run('test:app', host='127.0.0.1', port=4567, reload=True)