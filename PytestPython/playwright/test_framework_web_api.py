import os
import pytest

from pages.loginPage import LoginPage
from utils.data_loader import USER_CREDENTIAL_LIST
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("user_credentials", [USER_CREDENTIAL_LIST[0]])
def test_e2e_web_api(page: Page, order_id, user_credentials):
    email = os.getenv("APP_USER_EMAIL", user_credentials["email"])
    password = os.getenv("APP_USER_PASSWORD", user_credentials["password"])

    loginPage = LoginPage(page)

    order_table = page.get_by_role("row")

    # login
    page.goto("https://rahulshettyacademy.com/client/")
    loginPage.login(email, password)

    expect(page.get_by_role("button", name="HOME")).to_be_visible()
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_role("heading", name="Your Orders")).to_be_visible()

    expect(order_table.filter(has_text=order_id)).to_be_visible()
    order_table.filter(has_text=order_id).get_by_role("button", name="View").click()
    expect(page.get_by_role("paragraph").filter(has_text="Thank you for Shopping With Us")).to_be_visible()
