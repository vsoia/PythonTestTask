def test_get_user_2(session, base_url):
    response = session.get(f"{base_url}/users/2")
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["id"] == 2





