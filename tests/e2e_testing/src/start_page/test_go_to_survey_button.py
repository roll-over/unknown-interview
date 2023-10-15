from playwright.sync_api import Page, expect
import os

EXTERNAL_URL = os.environ["EXTERNAL_URL"]


def test_has_go_to_survey_button(page: Page):
    page.goto(EXTERNAL_URL)
    expect(page.get_by_role("link", name="go to survey!")).to_be_visible()


def test_go_to_survey_button_redirects_to_create_page(page: Page):
    page.goto(EXTERNAL_URL)
    page.get_by_role("link", name="go to survey!").click()
    expect(page).to_have_url(f"{EXTERNAL_URL}/create")
