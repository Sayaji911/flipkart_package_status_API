import requests as _requests
import bs4 as _bs4
from typing import List, Dict
import json as _json
import  pandas as pd
import csv




def _generate_url(track_id : str) -> str:
    url = f"https://ekartlogistics.com/track/{track_id}"
    return url

def _get_page(url : str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content,  "html.parser")
    return soup

def complete_tracking(track_id: str):
    headers = []
    _data = []
    url = _generate_url(track_id)
    page = _get_page(url)
    # raw_record = page.find_all(class_ = "col-md-12 table-bordered table-striped table-condensed cf width-100")
    table = page.select('table')[-1]
    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)



    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        _data.append(row_data)

        for n in range(20):
            data_zip = dict(zip(headers, row_data))


        with open("events.json", mode = "w") as events_file:
              _json.dump(data_zip, events_file, indent=False)



print(complete_tracking('FMPP0701772870'))

def current_status(track_id: str):
    headers = []
    url = _generate_url(track_id)
    page = _get_page(url)
    #gets table from the url
    table = page.find('table', {'class': 'col-md-12 table-bordered table-striped table-condensed cf width-100'})
    #puts the table headers in header list
    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)
    #puts all data in row data
    for row in table.find_all('tr')[1:]:
        data  = row.find_all('td')
        row_data = [td.text.strip() for td in data]
    #covert list data to json
    jsonList = []
    for i in range(0, len(headers)):
        jsonList.append({"header": headers[i], "status": row_data[i]})
    return jsonList







