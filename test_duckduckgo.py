import requests
import json
import pytest


##########################################
####      US Presidents Last Names     ###
##########################################


us_presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Quincy Adams', 'Jackson', 'Van Buren',
                 'Henry Harrison', 'Tyler', 'K. Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson',
                 'S. Grant', 'B. Hayes', 'A. Garfield', 'Arthur', 'Cleveland', 'Harrison', 'McKinley', 'Roosevelt',
                 'Howard Taft', 'Wilson', 'G. Harding', 'Coolidge', 'Hoover', 'D. Roosevelt', 'Truman', 'D. Eisenhower',
                 'F. Kennedy', 'B. Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'H. W. Bush', 'Clinton', 'W. Bush',
                 'Obama', 'Trump', 'Biden']


###############################
####        Fixtures       ####
###############################


@pytest.fixture
def ddb_request():
    url_ddg = "https://api.duckduckgo.com"
    request = requests.get(url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json")
    return request


@pytest.fixture
def ddg_fixture_res(ddb_request):
    resp = ddb_request.json()
    rsp_data = json.dumps(resp['RelatedTopics'])
    return rsp_data


@pytest.fixture
def president_dic(ddg_fixture_res):
    president_dic = {}
    for president in us_presidents:
        if president in ddg_fixture_res:
            president_dic[president] = True
        else:
            president_dic[president] = False
    return dict(president_dic)


###############################
####        Tests          ####
###############################


def test_ddg_appear_names_presidents(ddg_fixture_res):
    for i in range(len(us_presidents)):
        assert us_presidents[i] in ddg_fixture_res


def test_all_presidents_true(president_dic):
    assert True == all(president_dic)


def test_45_presidents(president_dic):
    assert 45 == len(president_dic)


def test_successful_call(ddb_request):
    assert ddb_request.status_code == 200
