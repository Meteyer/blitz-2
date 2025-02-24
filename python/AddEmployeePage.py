class AddEmployeePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/add_employee")

    def create_default_employee(self):
        self.create_employee()

    def create_employee(self, name="Flo", email="flo@flo.fr", adress_line1="44 Avenue de Paris", adress_line2="",
                        city="Paris", zip_code="75018", hiring_date="2025-02-25", job_title="Ingénieur"):

        self.page.locator("input[name='name']").fill(name)
        self.page.locator("input[name='email']").fill(email)
        self.page.locator("input[name='address_line1']").fill(adress_line1)
        self.page.locator("input[name='address_line2']").fill(adress_line2)
        self.page.locator("input[name='city']").fill(city)
        self.page.locator("input[name='zip_code']").fill(zip_code)
        self.page.locator("input[name='hiring_date']").fill(hiring_date)
        self.page.locator("input[name='job_title']").fill(job_title)

        self.page.click("text='Add'")

