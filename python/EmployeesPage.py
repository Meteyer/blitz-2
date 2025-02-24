class EmployeesPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/employees")

    def get_employee_email(self, row: int) -> str:
        return self.page.locator(f"body > table > tbody > tr:nth-child({row}) > td:nth-child(2)").text_content()

    def navigate_to_edit_employee(self, row: int):
        row = self.page.locator(f".table > tbody tr:nth-child({row})")
        row.get_by_role("link", name="Edit").click()

    def is_manager(self, row: int):
        return "yes" in self.page.locator(f".table > tbody:nth-child(2) > tr:nth-child({row}) > td:nth-child(3)")\
            .text_content()

    def get_number_of_employees(self):
        return self.page.locator("table tbody").count()
