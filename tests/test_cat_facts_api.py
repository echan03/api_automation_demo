import requests
import json
from utilities.configurations import *

def getCatReponse() -> requests.Response:
    return requests.get(getConfig()['API']['catEndpoint'], params={'count': 3})    
    
def test_fact_count():
    dict_response = json.loads(getCatReponse().text)
    assert len(dict_response['data']) == 3
    
def test_status_code():
    assert getCatReponse().status_code == 200
    
def test_header_content_type():
    assert getCatReponse().headers['Content-Type'] == 'application/json; charset=utf-8'
    
    