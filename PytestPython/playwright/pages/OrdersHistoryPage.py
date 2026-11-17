from playwright.sync_api import Page, Locator


class OrdersHistoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.orders_heading = page.get_by_role("heading", name="Your Orders")
        self.order_rows = page.get_by_role("row")

    def get_order_row(self, order_id: str) -> Locator:
        return self.order_rows.filter(has_text=order_id)

    def view_order(self, order_id: str):
        self.get_order_row(order_id).get_by_role("button", name="View").click()
