import requests
import json

testing_env_companies_url = "http://127.0.0.1:8000/companies/"

'''
PLEASE NOTE: THESE TEST ARE JUST A MORE "GENERIC" WAY TO TEST API's WHILE USING PYTEST AND REQUESTS LIBRARY.
KEEP IN MIND THAT IN ORDER TO RUN THESES TESTS YOU MUST HAVE A DJANGO SERVER UP AND RUNNING.
'''


def test_zero_companies_django_agnostic() -> None:
    response = requests.get(url=testing_env_companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_create_company_with_layoffs_django_agnostic() -> None:
    response = requests.post(
        url=testing_env_companies_url,
        json={"name": "test company name", "status": "Layoffs"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"

    cleanup_company(company_id=response_content["id"])


def cleanup_company(company_id: str) -> None:
    response = requests.delete(url=f"http://127.0.0.1:8000/companies/{company_id}")
    assert response.status_code == 204
