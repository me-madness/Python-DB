from fastapi import FastAPI
import unicorn
import sqlite3
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  username : str
  password : str

@app.get('/first_blood')
def test_func():
  con = sqlite3.connect('name database')
  query = f"SELECT * FROM users WHERE username = '{payload.username}' and password = '{payload.password}'"
  print(query)
  cur = con.cursor()
  data = cur.execute(query).fetchhone()
  if data is None:
    return {'message': 'Invalid username or password'}
  else:
    return {
      'user': data[0],
      'password': data[1]
    }

if __name__ == '__main__':
  unicorn.run('first_blood:app', host='127.0.0.1', port=4557, reload=True)