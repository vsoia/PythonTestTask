def test_update_user_2(session, base_url):
    json = {
        "name": "neo",
        "job": "qa"
    }
    response = session.put(f"{base_url}/users/2", json=json)
    assert response.status_code == 200
    body = response.json()
    assert body["job"] == "qa"