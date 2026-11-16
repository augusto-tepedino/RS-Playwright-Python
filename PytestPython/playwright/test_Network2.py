import os

from playwright.sync_api import Page, expect, Playwright
from utils.apiBase import APIUtils

email = os.getenv("APP_USER_EMAIL", "rahulshetty@gmail.com")
password = os.getenv("APP_USER_PASSWORD", "Iamking@000")

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6afa112392a4341c4c1af3ff")

def test_Network2(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")

    page.get_by_role("textbox", name="email").fill(email)
    page.get_by_role("textbox", name="passsword").fill(password)
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    product_by_name = page.get_by_role("row").filter(has_text="ADIDAS ORIGINAL")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
               intercept_request)

    product_by_name.get_by_role("button", name="View").click()
    expect(page.get_by_role("paragraph").filter(has_text="You are not authorize to view this order")).to_be_visible()

def test_session_storage(playwright: Playwright):
    apiUtils = APIUtils()
    getToken = apiUtils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #inject token
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")

    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_role("row").filter(has_text="ADIDAS ORIGINAL")).to_be_visible()
