from fastapi import FastAPI, HTTPException, status
import scrapper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to this cool package tracker api"}


@app.get("/current_status/{track_id}")
async def cur_status(track_id: str):
    if not scrapper.current_status(track_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Tracking ID")
    else:
        return scrapper.current_status(track_id)


@app.get("/complete_tracking/{track_id}")
async def com_tracking(track_id: str):
    if not scrapper.complete_tracking(track_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Tracking ID")
    else:
        return scrapper.current_status(track_id)
