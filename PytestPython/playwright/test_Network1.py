import os
from playwright.sync_api import Page, expect


# @pytest.fixture(scope="function", autouse=True)
# def beforeEach(page: Page):
#     page.goto("https://rahulshettyacademy.com/client/auth/login")
fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_Network1(page: Page):
    email = os.getenv("APP_USER_EMAIL", "rahulshetty@gmail.com")
    password = os.getenv("APP_USER_PASSWORD", "Iamking@000")

    page.goto("https://rahulshettyacademy.com/client/")

    page.get_by_role("textbox", name="email").fill(email)
    page.get_by_role("textbox", name="passsword").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="HOME")).to_be_visible()

    page.route("https://rahulshettyacademy.com//api/ecom/order/get-orders-for-customer/*",
               intercept_response)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("You have No Orders to show at")).to_be_visible()
