"""
This test is made to make sure it's not possible to duplicate an employee
"""


def test_duplicate_employee(page, reset_db, create_default_employee):

    # Create an employee
    page.goto("/")
    page.goto("/add_employee")

    create_default_employee()

    # Duplicate employee
    page.goto("/")
    page.goto("/add_employee")
    create_default_employee()

    # Goto the employees list

    page.goto("/")
    page.goto("/employees")

    assert page.locator("body > table > tbody > tr:nth-child(1) > td:nth-child(2)").text_content() == "flo@flo.fr"
    assert not page.locator("body > table > tbody > tr:nth-child(2) > td:nth-child(2)").text_content() == "flo@flo.fr",\
        "Second employee is a duplicate of first employee. It shouldn't be possible"
