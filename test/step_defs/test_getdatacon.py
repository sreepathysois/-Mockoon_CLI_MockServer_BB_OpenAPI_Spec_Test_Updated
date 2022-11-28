import pytest
import json 
import requests
import sys
from pytest_bdd import scenarios, given, when, then, parsers
# Constants
#API_HOME = 'http://172.16.51.57:8000/home/'
API_HOME = 'http://myapi:3000/api/v1/data/con/1.0'
 
# Scenarios
 
scenarios('../features/getdatacon.feature')
 
# Fixtures
 
@pytest.fixture

@given('the API URL home page is queried', target_fixture='ddg_response')
def ddg_response():
    params = {'format': 'json'}
    response = requests.get(API_HOME)
    return response


# Then Steps



@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code


@when(parsers.parse('the response contains result count data as'))
def ddg_response_contents():
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    response = requests.get(API_HOME)  
    print(response)
    json_data = response.json()
    #assert json_data['results'][1] == '095be615-a8ad-4c33-8e9c-c7612fbf6c9f' 
    assert json_data['count'] == 123  

