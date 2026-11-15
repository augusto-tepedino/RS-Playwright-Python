from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    print("test")


def test_playwrightFFBasics(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    print("test")


def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")
    print("test")


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").fill("Learning@830$3mK2")
    page.get_by_role("radio", name="Admin").click()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_role("heading", name="Shop Name")).to_be_visible()


def test_coreLocatorslogged(page: Page):
    iphoneCard = page.locator(".card.h-100").filter(has_text="iphone X")
    iphoneCard.get_by_role("button", name="Add").click
    expect(page.get_by_text("Checkout ( 1 )")).to_be_visible()


def test_childWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page_info:
        page.get_by_role("link", name="Free Access to Interview").click()

    childPage = new_page_info.value
    redText = childPage.get_by_text("Please email us at").text_content()
    redTextEmail = redText.split("at")[1].strip().split(" ")[0]
    print(redTextEmail)

    expect(childPage.get_by_role("heading", name="Documents request")).to_be_visible()
    assert redTextEmail == "mentor@rahulshettyacademy.com"
