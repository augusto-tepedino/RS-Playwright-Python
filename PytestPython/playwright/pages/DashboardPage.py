from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.home_button = page.get_by_role("button", name="HOME")

    def navigate_to_orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
