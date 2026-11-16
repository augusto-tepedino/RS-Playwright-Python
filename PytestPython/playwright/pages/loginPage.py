import pytest
from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email, password):
        self.page.get_by_role("textbox", name="email").fill(email)
        self.page.get_by_role("textbox", name="passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()