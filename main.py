from fastapi import FastAPI
import scrapper

app = FastAPI()

@app.get("/")
async def root():
    return  {"message": "welcome to this cool package tracker api"}

@app.get("/current_status/{track_id}")
async  def cur_status(track_id : str):
    return scrapper.current_status(track_id)

@app.get("/complete_tracking/{track_id}")
async def com_tracking(track_id : str):
    return scrapper.complete_tracking(track_id)


