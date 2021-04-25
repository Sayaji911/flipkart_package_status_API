import json
import re

from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse

import scrapper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to this cool package tracker api"}


@app.post("/current_status/")
async def cur_status(Body: str = Form(...)):
    response = MessagingResponse()
    if not scrapper.current_status(Body):
        response.message(f"Invalid Tracking ID '{Body}'")
        return Response(content=str(response), media_type="application/xml")
    elif scrapper.current_status(Body) == 0:
        response.message('Connection Issue, Retry in 30 Seconds')
        return Response(content=str(response), media_type="application/xml")
    else:
        raw_result = scrapper.current_status(Body)
        result = re.sub('[](){}"<>[]', '', json.dumps(raw_result))
        response.message(result)
        return Response(content=str(response), media_type="application/xml")


@app.post("/complete_tracking/")
async def com_tracking(Body: str = Form(...)):
    response_ = MessagingResponse()
    if not scrapper.complete_tracking(Body):
        response_.message(f"Invalid Tracking ID '{Body}'")
        return Response(content=str(response_), media_type="application/xml")
    elif scrapper.complete_tracking(Body) == 0:
        response_.message('Connection Issue, Retry in 30 Seconds')
        return Response(content=str(response_), media_type="application/xml")
    else:
        raw_result = scrapper.complete_tracking(Body)
        result = re.sub('[](){}"<>[]', '', json.dumps(raw_result))
        response_.message(result)
        return Response(content=str(response_), media_type="application/xml")
