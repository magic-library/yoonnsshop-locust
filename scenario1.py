from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(0.1, 5)  # 각 태스크 사이의 대기 시간 설정 (초 단위)

    def on_start(self):
        # 로그인 등의 초기 설정 작업 수행
        pass

    @task(80)
    def scenario_1(self):
        self.client.get("/items")  # 상품 리스트 조회
        self.client.get("/items/1")  # 상품 상세 조회
        self.client.post("/carts/1", params={"quantity": 1})  # 장바구니 추가
        self.client.get("/carts")  # 장바구니 확인
        self.client.post("/orders", json={"orderItems": [{"itemId": 1, "quantity": 10}]})  # 주문

    @task(15)
    def scenario_2(self):
        self.client.get("/items")  # 상품 리스트 조회
        self.client.get("/items/1")  # 상품 상세 조회
        self.client.post("/carts/1", params={"quantity": 1})  # 장바구니 추가
        self.client.get("/carts")  # 장바구니 확인
        self.client.put("/carts/1", params={"quantity": 2})  # 장바구니 추가
        self.client.post("/orders", json={"orderItems": [{"itemId": 1, "quantity": 10}]})  # 주문

    @task(5)
    def scenario_3(self):
        # 5%의 사용자 시나리오
        self.client.get("/items")  # 상품 리스트 조회
        self.client.get("/items/1")  # 상품 상세 조회
        self.client.post("/carts/1", params={"quantity": 1})  # 장바구니 추가
        self.client.get("/carts")  # 장바구니 확인
        self.client.delete("/carts/1")  # 장바구니 삭제

# class AdminUser(HttpUser):
#     wait_time = between(1, 2)  # 관리자 사용자의 대기 시간 설정 (초 단위)
#
#     def on_start(self):
#         # 관리자 로그인 등의 초기 설정 작업 수행
#         pass
#
#     @task
#     def admin_scenario(self):
#         # 관리자 시나리오
#         self.client.post("/items", json={"name": "New Product", "price": 10})  # 신규 상품 등록
#         self.client.get("/admin/items")  # 등록된 상품 리스트 조회
#         self.client.put("/admin/items/1", json={"price": 20})  # 상품 정보 수정
#         self.client.delete("/admin/items/1")  # 상품 삭제