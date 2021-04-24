import requests as _requests
import bs4 as _bs4


def _generate_url(track_id: str) -> str:
    url = f"https://ekartlogistics.com/track/{track_id}"
    return url


def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def complete_tracking(track_id: str):
    raw_list = []
    headers = []
    _data = []
    url = _generate_url(track_id)
    page = _get_page(url)
    # raw_record = page.find_all(class_ = "col-md-12 table-bordered table-striped table-condensed cf width-100")
    try:

        table = page.select('table')[-1]
        for i in table.find_all('th'):
            title = i.text.strip()
            headers.append(title)

        for row in table.find_all('tr')[1:]:
            data = row.find_all('td')
            row_data = [td.text.strip() for td in data]
            raw_list.append(row_data)
        #    return raw_list

        for i in range(len(raw_list)):
            zipped_ = dict(zip(headers, raw_list[i]))
            _data.append(zipped_)

        return _data
    except IndexError:
        return None


def current_status(track_id: str):
    headers = []
    zipped_one = None
    url = _generate_url(track_id)
    page = _get_page(url)
    # gets table from the url
    try:
        table = page.find('table', {'class': 'col-md-12 table-bordered table-striped table-condensed cf width-100'})
        # puts the table headers in header list
        for i in table.find_all('th'):
            title = i.text.strip()
            headers.append(title)
        # puts all data in row data
        for row in table.find_all('tr')[1:]:
            data = row.find_all('td')
            row_data = [td.text.strip() for td in data]
            # covert list data to json
            _data_one = []
            for i in range(len(headers)):
                zipped_one = dict(zip(headers, row_data))
            _data_one.append(zipped_one)
            return _data_one
    except IndexError:
        return None

print(complete_tracking("FMPP0701772857"))