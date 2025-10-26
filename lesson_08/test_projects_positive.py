from yougile_api import YougileAPI

BASE_URL = "https://ru.yougile.com"
API_KEY = "" # ВСТАВИТЬ СВОЙ API-KEY


def test_create_project():
    api = YougileAPI(BASE_URL, API_KEY)
    result = api.create_project("Test Project")
    assert result["status_code"] == 201
    assert "id" in result["response"]


def test_get_project():
    api = YougileAPI(BASE_URL, API_KEY)
    create_result = api.create_project("Project for Get")
    project_id = create_result["response"]["id"]
    result = api.get_project(project_id)
    assert result["status_code"] == 200
    assert result["response"]["id"] == project_id


def test_update_project():
    api = YougileAPI(BASE_URL, API_KEY)
    create_result = api.create_project("Project to Update")
    project_id = create_result["response"]["id"]
    result = api.update_project(project_id, title="New Title")
    assert result["status_code"] == 200
