import pytest


@pytest.fixture
def reset_db(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()


def test_delete_employee(page, reset_db):

    # Create an employee
    page.goto("/")
    page.goto("/add_employee")

    create_employee(page)

    # Duplicate employee
    page.goto("/")
    page.goto("/add_employee")
    create_employee(page)

    # Goto the employees list

    page.goto("/")
    page.goto("/employees")

    assert page.locator("body > table > tbody > tr:nth-child(1) > td:nth-child(2)").text_content() == "flo@flo.fr"
    assert page.locator("body > table > tbody > tr:nth-child(2) > td:nth-child(2)").text_content() == "flo@flo.fr"


def create_employee(page):
    page.locator("input[name='name']").fill("Flo")
    page.locator("input[name='email']").fill("flo@flo.fr")
    page.locator("input[name='address_line1']").fill("44 Avenue de Paris")
    page.locator("input[name='city']").fill("Paris")
    page.locator("input[name='zip_code']").fill("75018")
    page.locator("input[name='hiring_date']").fill("2025-02-25")
    page.locator("input[name='job_title']").fill("Ingénieur")

    page.click("text='Add'")
