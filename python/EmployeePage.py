class EmployeePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, employee_id: int):
        self.page.goto(f"/employees/{employee_id}")

    def promote_to_manager(self):
        self.page.get_by_role("link", name="Promote as manager").click()
        self.page.get_by_role("button", name="Proceed").click()

