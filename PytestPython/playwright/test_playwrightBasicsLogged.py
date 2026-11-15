import pytest
from playwright.sync_api import Page, expect, Playwright


@pytest.fixture(scope="function", autouse=True)
def beforeEach(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").fill("Learning@830$3mK2")
    page.get_by_role("radio", name="Admin").click()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_role("heading", name="Shop Name")).to_be_visible()


def test_addItemCart(page: Page):
    products = {"product1": "iphone X", "product2": "Blackberry"}
    itemCard = page.locator("app-card")
    iphoneCard = itemCard.filter(has_text=products["product1"])
    blackberryCard = itemCard.filter(has_text=products["product2"])
    checkout_button = page.get_by_text("Checkout")
    table = page.get_by_role("row")
    table_item_name = page.get_by_role("row").locator(".media-body")

    iphoneCard.get_by_role("button", name="Add").click()
    blackberryCard.get_by_role("button", name="Add").click()

    expect(checkout_button).to_contain_text("( 2 )")
    checkout_button.click()

    expect(table_item_name).to_have_count(len(products))
    expect(table.filter(has_text=products["product1"])).to_be_visible()
    expect(table.filter(has_text=products["product2"])).to_be_visible()
