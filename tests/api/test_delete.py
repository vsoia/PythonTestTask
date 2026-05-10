def test_delete_user_2(session, base_url):
    response = session.delete(f"{base_url}/users/2")
    assert response.status_code == 204
    assert response.text == ""