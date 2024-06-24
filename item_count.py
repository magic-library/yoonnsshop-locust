from locust import HttpUser, task, between
from faker import Faker

class AdminUser(HttpUser):
    wait_time = between(1, 2)  # 관리자 사용자의 대기 시간 설정 (초 단위)
    del_item_ids = 100  # 1부터 300까지의 아이템 ID 목록
    fake = Faker()
    def random_string(self):
        return self.fake.pystr(min_chars=5, max_chars=10)

    def on_start(self):
        # 관리자 로그인 등의 초기 설정 작업 수행
        pass

    @task(30)
    def insert_item(self):
        item_name = "New Product " + self.random_string()
        response = self.client.post("/admins/items", json={"name": item_name, "price": 10, "description": "New Product Description", "stockQuantity": 100})
        if response.status_code == 200:
            print("insert success")


    @task(20)
    def delete_item(self):
        item_id = self.del_item_ids
        response = self.client.delete(f"/admins/items/{item_id}")
        if response.status_code == 200:
            print("delete success")
            self.del_item_ids += 1

    @task(50)
    def get_itemlist(self):
        response = self.client.get("/admins/items/v2")  # 등록된 상품 리스트 조회
        print(f"item_count: {response.json()['totalElements']}")