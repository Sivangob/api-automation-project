def test_get_all_posts_returns_list(posts_api):
    response = posts_api.get_all_posts()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_post_contains_required_fields(posts_api):
    response = posts_api.get_post_by_id(1)
    post = response.json()

    assert response.status_code == 200
    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post


def test_invalid_post_id_returns_404(posts_api):
    response = posts_api.get_post_by_id(999999)

    assert response.status_code == 404


def test_get_posts_response_time(posts_api):
    response = posts_api.get_all_posts()

    response_time_ms = posts_api.get_response_time_ms(response)

    assert response.status_code == 200
    assert response_time_ms < 500  # SLA: פחות מ־500ms


def test_average_response_time(posts_api):
    response_times = []

    for _ in range(5):
        response = posts_api.get_all_posts()
        response_times.append(
            posts_api.get_response_time_ms(response)
        )

    average_time = sum(response_times) / len(response_times)

    assert average_time < 500
