#!/usr/bin/env python

'''Flask API test module'''

import json
import pytest
import unittest
from api.flask_api import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_authenticate(client):

    '''Tests authentication URL'''

    res = client.get("/")
    assert(res.status_code == 302)


def test_create_invalid_data(client):

    '''Tests create endpoint with invalid data'''

    res = client.post("/create")
    assert(res.status_code == 415)


def test_create_no_token(client):

    '''Tests create endpoint with no token'''

    res = client.post("/create", content_type='application/json',
                      data = json.dumps({'user' : 'xyzx', 'name' : 'hjdk'}))
    assert(res.status_code == 400)


def test_create_add_invalid_data(client):

    '''Tests create_add endpoint with invalid data'''

    res = client.post("/create_add")
    assert(res.status_code == 415)


def test_create_add_no_user(client):

    '''Tests create_add endpoint with no user'''

    res = client.post("/create_add", content_type='application/json', data = json.dumps({}))
    assert(res.status_code == 400)
    assert(res.data.decode("utf-8") == "Please enter user")


def test_create_add_no_playlist_name(client):

    '''Tests create_add endpoint with no playlist name'''

    res = client.post("/create_add", content_type='application/json',
                      data = json.dumps({'user' : 'hi'}))
    assert(res.status_code == 400)
    assert(res.data.decode("utf-8") == "Please enter name of playlist as name")


def test_create_add_no_token(client):

    '''Tests create_add endpoint with no token'''

    res = client.post("/create_add", content_type='application/json',
                      data = json.dumps({'user' : 'xyzx', 'name' : 'hjdk'}))
    assert(res.status_code == 400)


def test_add_invalid_data(client):

    '''Tests add endpoint with invalid data'''

    res = client.put("/add")
    assert(res.status_code == 415)


def test_add_no_user(client):

    '''Tests add endpoint with no user'''

    res = client.put("/add", content_type='application/json', data = json.dumps({}))
    assert(res.status_code == 400)
    assert(res.data.decode("utf-8") == "Please enter user")


def test_add_no_playlist_id(client):

    '''Tests add endpoint with no playlist_id'''

    res = client.put("/add", content_type='application/json',
                      data = json.dumps({'user' : 'hi'}))
    assert(res.status_code == 400)
    assert(res.data.decode("utf-8") == "Please enter id of playlist to be updated")


def test_add_no_token(client):

    '''Tests add endpoint with no token'''

    res = client.put("/add", content_type='application/json',
                     data = json.dumps({'user' : 'xyzx', 'name' : 'hjdk'}))
    assert(res.status_code == 400)


def test_get_invalid(client):

    '''Tests getting invalid songs'''

    res = client.get("/songs", content_type='application/json',
                     data = json.dumps({"xyz" : "Khalid"}))
    assert(res.status_code == 400)


def test_get_one(client):

    '''Tests getting one song'''

    res = client.get("/songs", content_type='application/json',
                     data = json.dumps({"Better" : "Khalid"}))
    assert(res.status_code == 200)
    assert(json.loads(res.data.decode("utf-8").replace("\'", "\""))
            == ['6zeeWid2sgw4lap2jV61PZ'])


def test_get_multiple(client):

    '''Tests getting multiple songs'''

    res = client.get("/songs", content_type='application/json',
                     data = json.dumps({"Better" : "Khalid",
                                        "Peaches" : "Justin Bieber"}))
    assert(res.status_code == 200)
    assert(json.loads(res.data.decode("utf-8").replace("\'", "\""))
            == ['6zeeWid2sgw4lap2jV61PZ', '4iJyoBOLtHqaGxP12qzhQI'])
