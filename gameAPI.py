import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
import sqlite3



app = FastAPI()


class Inputs(BaseModel):
    inp: int
    inp2: str


@app.get("/")
async def index():
    with sqlite3.connect("db_game.db") as conn:

        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        query = 'SELECT * FROM jogadores'
        cur.execute(query)


        data = [dict(d) for d  in cur.fetchall()]
        print(data)

    return data


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=7777)
