import pytest
from src.api.posts_api import PostsApi
from src.config import BASE_URL


@pytest.fixture
def posts_api():
    return PostsApi(BASE_URL)
