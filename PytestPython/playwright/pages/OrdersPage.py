from playwright.sync_api import Page


class OrdersPage:
    def __init__(self, page: Page):
        self.page = page
        self.success_message = page.get_by_role("paragraph").filter(
            has_text="Thank you for Shopping With Us"
        )
