import requests
import json
from utilities.configurations import *

def getGithubUsers() -> requests.Response:
    return requests.get(getConfig()['API']['githubEndpoint'] + getConfig()['API']['users'], auth=(getUsername(), getToken()))

def createEmptyRepo(repoName: str) -> requests.Response:
    data = {
        "name": repoName
    }
    return requests.post(getConfig()['API']['githubEndpoint'] + getConfig()['API']['userRepos'], auth=(getUsername(), getToken()), json=data)

def deleteRepo(repoName: str) -> requests.Response:
    endpoint = getConfig()['API']['githubEndpoint'] + getConfig()['API']['repos'] + "/" + getUsername() + "/" + repoName
    return requests.delete(endpoint, auth=(getUsername(), getToken()))

def test_get_users():
    print(getGithubUsers().text)
    assert getGithubUsers().status_code == 200
    
def test_create_repo():
    response = createEmptyRepo("i-made-this-repo-from-an-api")
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())
    assert response.status_code == 201
    
def test_delete_repo():
    response = deleteRepo("i-made-this-repo-from-an-api")
    print("Status Code", response.status_code)
    assert response.status_code == 204