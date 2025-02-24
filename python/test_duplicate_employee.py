"""
This test is made to make sure it's not possible to duplicate an employee
"""


def test_duplicate_employee(page, reset_db, add_employee_page, employees_page):

    # Create an employee
    add_employee_page.navigate()
    add_employee_page.create_default_employee()

    # Duplicate employee
    add_employee_page.navigate()
    add_employee_page.create_default_employee()

    # Goto the employees list

    employees_page.navigate()

    assert employees_page.get_employee_email(1) == "flo@flo.fr"
    assert not employees_page.get_employee_email(2) == "flo@flo.fr",\
        "Second employee is a duplicate of first employee. It shouldn't be possible"
