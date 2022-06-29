import json
import pytest
import random
import string

from django.urls import reverse

from companies.models import Company


companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return str(result_str)


def test_zero_companies_should_return_empty_list(client):
    response = client.get(companies_url)

    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_exists(client):
    company = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]

    assert response.status_code == 200
    assert response_content.get("name") == company.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_name_and_default_values(client):
    random_name = str(get_random_string(10))
    response = client.post(path=companies_url, data={"name": random_name})
    response_content = json.loads(response.content)

    assert response.status_code == 201
    assert response_content.get("name") == random_name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_name_and_status(client):
    random_name = str(get_random_string(10))
    response = client.post(path=companies_url, data={"name": random_name, "status": "Layoffs"})
    response_content = json.loads(response.content)

    assert response.status_code == 201
    assert response_content.get("name") == random_name
    assert response_content.get("status") == "Layoffs"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_more_than_allowed_chars(client):
    Company.objects.create(name="Companywith31charswhichismorethantheallowednumberofchars")
    response = client.post(path=companies_url,
                                    data={"name": "Companywith31charswhichismorethantheallowednumberofchars"})

    assert response.status_code == 400
    assert (json.loads(response.content) == {
        'name': ['company with this name already exists.', 'Ensure this field has no more than 30 characters.']})


def test_create_company_without_arguments(client):
    response = client.post(path=companies_url)

    assert response.status_code == 400
    assert (json.loads(response.content) == {"name": ["This field is required."]})


def test_create_existing_company(client):
    Company.objects.create(name="Canonical")
    response = client.post(path=companies_url, data={"name": "Canonical"})

    assert response.status_code == 400
    assert (json.loads(response.content) == {"name": ["company with this name already exists."]})


def test_create_company_with_invalid_status(client):
    response = client.post(path=companies_url, data={"name": "test-company", "status": "InvalidStatus"})

    assert response.status_code == 400
    assert "InvalidStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)
