import pytest
import requests

def test_get1(simple_client):
    response = simple_client.get('/posts').json()
    assert len(response) == 100

def test_get2(simple_client):
    response = simple_client.get('/posts/1/comments')
    assert response.status_code == 200

def test_get3(simple_client):
    response = simple_client.get('/posts/1/comments')
    print(response.text)


def test_post1(simple_client):
    data = {'userId': 1, id: 101, 'title': 'test comment', 'body': 'here is my test comment' }
    response = simple_client.post('/posts/', data)
    assert response.status_code == 201
