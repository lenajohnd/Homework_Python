from yougile_api import YougileAPI

BASE_URL = "https://ru.yougile.com"
API_KEY = "" # ВСТАВИТЬ СВОЙ API-KEY


def test_create_empty_title():
    api = YougileAPI(BASE_URL, API_KEY)
    result = api.create_project("")
    assert result["status_code"] == 400


def test_get_nonexistent_project():
    api = YougileAPI(BASE_URL, API_KEY)
    result = api.get_project("fake_id_123")
    assert result["status_code"] == 404


def test_update_nonexistent_project():
    api = YougileAPI(BASE_URL, API_KEY)
    result = api.update_project("fake_id_123", title="New Title")
    assert result["status_code"] == 404


def test_create_invalid_users():
    api = YougileAPI(BASE_URL, API_KEY)
    result = api.create_project("Test", {"invalid_user": "admin"})
    assert result["status_code"] == 400
