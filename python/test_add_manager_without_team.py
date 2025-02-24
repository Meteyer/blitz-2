"""
This test is made to make sure it's not possible make an employee a manager if he's not assigned in a team.
"""


def test_add_manager_without_team(page, reset_db, add_employee_page, employees_page, employee_page):

    # Create an employee
    employee_row = 1

    add_employee_page.navigate()
    add_employee_page.create_default_employee()

    # Make the employee a manager
    employees_page.navigate()

    employees_page.navigate_to_edit_employee(employee_row)
    employee_page.promote_to_manager()

    # Check it is not a manager
    employees_page.navigate()
    is_manager = employees_page.is_manager(employee_row)

    assert is_manager is False, "Employee without team can't be a manager"

