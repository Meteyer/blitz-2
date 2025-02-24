"""
This test is made to make sure the zip code input in add employee form is safe.
"""


def test_zip_code(page, reset_db):

    # Create an employee
    page.goto("/")
    page.goto("/add_employee")

    page.locator("input[name='name']").fill("Flo")
    page.locator("input[name='email']").fill("flo@flo.fr")
    page.locator("input[name='address_line1']").fill("44 Avenue de Paris")
    page.locator("input[name='city']").fill("Paris")
    page.locator("input[name='zip_code']").fill("1000000")
    page.locator("input[name='hiring_date']").fill("2025-02-25")
    page.locator("input[name='job_title']").fill("Ingénieur")

    page.click("text='Add'")

    # Go to employees list
    page.goto("/")
    page.goto("/employees")

    # Make sure employee doesn't exist
    rows_count = page.locator("table tbody").count()

    assert rows_count == 0, "Employee should have not been created with wrong ZIP code."
