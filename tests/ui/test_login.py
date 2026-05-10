def test_login_success(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    assert page.locator("text=You logged into a secure area!").is_visible()
    assert page.locator(".icon-signout", has_text="Logout").is_visible()


def test_login_failed(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[name='username']", "test")
    page.fill("#password", "password")
    page.click("button[type='submit']")

    assert page.locator("text=Your username is invalid!").is_visible()
    assert page.locator("button[type='submit']").is_visible()
