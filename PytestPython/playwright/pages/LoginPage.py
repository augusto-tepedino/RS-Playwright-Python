from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self, email: str, password: str):
        self.page.get_by_role("textbox", name="email").fill(email)
        self.page.get_by_role("textbox", name="passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
