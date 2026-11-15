import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def beforeEach(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_role("heading", name="Practice Page")).to_be_visible()


def test_elementVisibility(page: Page):
    targetTextBox = page.get_by_role("textbox", name="Hide/Show Example")

    page.get_by_role("button", name="Show").click()
    expect(targetTextBox).to_be_visible()

    page.get_by_role("button", name="Hide").click()
    expect(targetTextBox).to_be_hidden()


def test_alert(page: Page):
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Alert").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()

def test_frames(page: Page):
    iframe = page.frame_locator("#courses-iframe")
    iframeHeading = iframe.get_by_role("heading", name="An Academy to Learn Earn")
    expect(iframeHeading).to_be_visible()
    expect(iframeHeading).to_have_text("An Academy to Learn Earn & Shine in your QA Career")


def test_tables(page: Page):
    column_head = page.get_by_role("columnheader")
    price_column_index = 0
    expected_wheat_value = 67
    page.goto("https://rahulshettyacademy.com/seleniumPractice/#/offers")
    for index in range(column_head.count()):
        if column_head.nth(index).filter(has_text="Price").count() > 0:
            price_column_index = index
            break
    tableRows = page.get_by_role("row")
    wheatPrice = tableRows.filter(has_text="Wheat").get_by_role("cell").nth(price_column_index)
    expect(wheatPrice).to_have_textt(expected_wheat_value)

