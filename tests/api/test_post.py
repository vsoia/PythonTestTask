def test_create_user(session, base_url):
    json = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = session.post(f"{base_url}/users", json=json)
    assert response.status_code in (200,201)
    body = response.json()
    assert body["name"] == "morpheus"
