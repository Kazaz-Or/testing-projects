import pytest
from django.urls import reverse

fibonacci_url = reverse('fib-seq')


def test_no_n_parameter_should_return_response(client) -> None:
    response = client.get(fibonacci_url)
    assert response.status_code == 200
    assert response.json() == "Hello there, no number was passed"


def test_post_method_with_fib_endpoint_should_fail(client) -> None:
    response = client.post(fibonacci_url, data={"n": 4})
    assert response.status_code == 405
    assert response.json()["detail"] == 'Method "POST" not allowed.'


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_stress_fibonacci_endpoint(client, n: int, expected: int) -> None:
    response = client.get(
        fibonacci_url,
        data={"n": n}
    )
    assert response.status_code == 200
    assert response.json()["result"] == expected
