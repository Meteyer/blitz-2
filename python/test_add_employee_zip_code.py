"""
This test is made to make sure the zip code input in add employee form is safe.
"""


def test_zip_code(page, reset_db, add_employee_page, employees_page):

    # Create an employee
    page.goto("/")
    add_employee_page.navigate()

    add_employee_page.create_employee(zip_code="1000000")

    # Go to employees list
    page.goto("/")
    employees_page.navigate()

    # Make sure employee doesn't exist
    employees_count = employees_page.get_number_of_employees()
    assert employees_count == 0, "Employee should have not been created with wrong ZIP code."
