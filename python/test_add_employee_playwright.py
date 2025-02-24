import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://b.lsi2.hr.dmerej.info/")
    page.get_by_role("link", name="Reset database").click()
    page.get_by_role("button", name="Proceed").click()
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").fill("Flo")
    page.get_by_role("textbox", name="Email").fill("flo@flo.fr")
    page.locator("#id_address_line1").fill("44 Avenue de Paris")
    page.get_by_role("textbox", name="City").fill("Paris")
    page.get_by_role("spinbutton", name="Zip code").fill("75018")
    page.get_by_role("textbox", name="Hiring date").fill("2025-02-25")
    page.get_by_role("textbox", name="Job title").fill("Ingénieur")
    page.get_by_role("button", name="Add").click()
    expect(page.locator("tbody")).to_contain_text("flo@flo.fr")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
