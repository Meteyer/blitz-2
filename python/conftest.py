import pytest

from AddEmployeePage import AddEmployeePage
from EmployeePage import EmployeePage
from EmployeesPage import EmployeesPage


@pytest.fixture
def reset_db(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()


@pytest.fixture
def employee_page(page):
    return EmployeePage(page)


@pytest.fixture
def add_employee_page(page):
    return AddEmployeePage(page)


@pytest.fixture
def employees_page(page):
    return EmployeesPage(page)


@pytest.fixture
def create_default_employee(page):
    def create():
        page.locator("input[name='name']").fill("Flo")
        page.locator("input[name='email']").fill("flo@flo.fr")
        page.locator("input[name='address_line1']").fill("44 Avenue de Paris")
        page.locator("input[name='city']").fill("Paris")
        page.locator("input[name='zip_code']").fill("75018")
        page.locator("input[name='hiring_date']").fill("2025-02-25")
        page.locator("input[name='job_title']").fill("Ingénieur")

        page.click("text='Add'")
    return create
