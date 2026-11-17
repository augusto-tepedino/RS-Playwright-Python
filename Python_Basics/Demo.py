class TestDemo:
    @classmethod
    def setup_class(cls):
        print("\n🟢 [1] setup_class EXECUTED (beforeAll)")

    def setup_method(self):
        print("\n🔵 [2] setup_method EXECUTED (beforeEach)")

    def teardown_method(self):
        print("\n🟠 [4] teardown_method EXECUTED (afterEach)")

    @classmethod
    def teardown_class(cls):
        print("\n🔴 [5] teardown_class EXECUTED (afterAll)")

    def test_one(self):
        print("   👉 Running test_one")

    def test_two(self):
        print("   👉 Running test_two")