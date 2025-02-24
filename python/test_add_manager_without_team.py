"""
This test is made to make sure it's not possible make an employee a manager if he's not assigned in a team.
"""


def test_add_manager_without_team(page, reset_db, create_default_employee):

    # Create an employee
    page.goto("/")
    page.goto("/add_employee")

    create_default_employee()

    # Make the employee a manager

    page.goto("/")
    page.goto("/employees")

    page.get_by_role("link", name="Edit").first.click()
    page.get_by_role("link", name="Promote as manager").click()
    page.get_by_role("button", name="Proceed").click()


    # Check it is not a manager
    page.goto("/")
    page.goto("/employees")

    assert page.locator(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text_content() == "no",\
        "Employee without team can't be a manager"

