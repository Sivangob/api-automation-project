from src.api.api_client import ApiClient


class PostsApi(ApiClient):

    def get_all_posts(self):
        return self.get("/posts")

    def get_post_by_id(self, post_id):
        return self.get(f"/posts/{post_id}")
