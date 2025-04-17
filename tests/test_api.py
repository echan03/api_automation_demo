import requests
import json
from utilities.configurations import *

def getCatReponse() -> requests.Response:
    return requests.get(getConfig()['API']['catEndpoint'], params={'count': 3})    

def getGithubUsers() -> requests.Response:
    return requests.get(getConfig()['API']['githubEndpoint'] + getConfig()['API']['users'], auth=(getUsername(), getToken()))

def createEmptyRepo(repoName: str) -> requests.Response:
    data = {
        "name": repoName
    }
    return requests.post(getConfig()['API']['githubEndpoint'] + getConfig()['API']['userRepos'], auth=(getUsername(), getToken()), json=data)

def deleteRepo(user: str, repoName: str) -> requests.Response:
    endpoint = getConfig()['API']['githubEndpoint'] + getConfig()['API']['repos'] + "/" + user + "/" + repoName
    return requests.delete(endpoint, auth=(getUsername(), getToken()))
    
def test_fact_count():
    dict_response = json.loads(getCatReponse().text)
    assert len(dict_response['data']) == 3
    
def test_status_code():
    assert getCatReponse().status_code == 200
    
def test_header_content_type():
    assert getCatReponse().headers['Content-Type'] == 'application/json; charset=utf-8'
    
def test_github_get_users():
    print(getGithubUsers().text)
    assert getGithubUsers().status_code == 200
    
def test_github_create_repo():
    response = createEmptyRepo("i-made-this-repo-from-an-api")
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())
    assert response.status_code == 201
    
def test_github_delete_repo():
    response = deleteRepo(getUsername(), "i-made-this-repo-from-an-api")
    print("Status Code", response.status_code)
    assert response.status_code == 204
    
    