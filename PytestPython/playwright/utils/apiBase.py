from playwright.sync_api import Playwright

ordersPayload = {
    "orders": [
        {
            "country": "Brazil",
            "productOrderedId": "6960eae1c941646b7a8b3ed3"
        }
    ]
}

class APIUtils:
    def getToken(self, playwright: Playwright, email, password):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail": email, "userPassword": password}
        )
        assert response.ok
        response_body = response.json()
        return response_body["token"]

    def createOrder(self, playwright: Playwright, email, password):
        token = self.getToken(playwright, email, password)
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
