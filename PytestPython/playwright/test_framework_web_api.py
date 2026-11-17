import os
import pytest
from playwright.sync_api import Page, expect

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.OrdersHistoryPage import OrdersHistoryPage
from pages.OrdersPage import OrdersPage
from utils.data_loader import USER_CREDENTIAL_LIST


@pytest.mark.parametrize("user_credentials", [USER_CREDENTIAL_LIST[0]])
def test_e2e_web_api(page: Page, order_id, user_credentials):
    email = os.getenv("APP_USER_EMAIL", user_credentials["email"])
    password = os.getenv("APP_USER_PASSWORD", user_credentials["password"])

    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email, password)

    # 2. Dashboard
    dashboard_page = DashboardPage(page)
    expect(dashboard_page.home_button).to_be_visible()
    dashboard_page.navigate_to_orders()

    # 3. Histórico de Pedidos
    orders_history_page = OrdersHistoryPage(page)
    expect(orders_history_page.orders_heading).to_be_visible()
    expect(orders_history_page.get_order_row(order_id)).to_be_visible()
    orders_history_page.view_order(order_id)

    # 4. Detalhes do Pedido
    orders_page = OrdersPage(page)
    expect(orders_page.success_message).to_be_visible()
