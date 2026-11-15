import os
from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils


# @pytest.fixture(scope="function", autouse=True)
# def beforeEach(page: Page):
#     page.goto("https://rahulshettyacademy.com/client/auth/login")

def test_e2e_web_api(playwright: Playwright):
    email = os.getenv("APP_USER_EMAIL", "rahulshetty@gmail.com")
    password = os.getenv("APP_USER_PASSWORD", "Iamking@000")

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Start tracing for CI/CD artifact debugging (visual steps, network, DOM snapshots)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    try:
        # create order -> orderID
        api_utils = APIUtils()
        order_id = api_utils.createOrder(playwright)

        # login
        page.goto("https://rahulshettyacademy.com/client/")
        page.get_by_role("textbox", name="email").fill(email)
        page.get_by_role("textbox", name="passsword").fill(password)
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_role("button", name="HOME")).to_be_visible()
        page.get_by_role("button", name="ORDERS").click()
        expect(page.get_by_role("heading", name="Your Orders")).to_be_visible()

        order_table = page.get_by_role("row")
        expect(order_table.filter(has_text=order_id)).to_be_visible()
        order_table.filter(has_text=order_id).get_by_role("button", name="View").click()
        # expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
        expect(page.get_by_role("paragraph").filter(has_text="Thank you for Shopping With Us")).to_be_visible()
    finally:
        # Save trace artifact
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()
