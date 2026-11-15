import os
from playwright.sync_api import Playwright

ordersPayload = {
    "orders": [
        {
            "country": "Brazil",
            "productOrderedId": "6960eae1c941646b7a8b3ed3"
        }
    ]
}

email = os.getenv("APP_USER_EMAIL", "rahulshetty@gmail.com")
password = os.getenv("APP_USER_PASSWORD", "Iamking@000")


class APIUtils:
    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail": email, "userPassword": password}
        )
        assert response.ok
        response_body = response.json()
        return response_body["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "api/ecom/order/create-order",
            data=ordersPayload,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )
        response_body = response.json()
        print(response_body)
        order_id = response_body["orders"][0]
        return order_id
