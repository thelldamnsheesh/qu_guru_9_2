import pytest
from selene import browser, have, be

@pytest.fixture
def browser_size():
    browser.driver.set_window_size(height=2560, width=1440)
    yield
    browser.quit()

def test_browser_search(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('auvybwoeurvoqiuerbqoerijvbfh').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))

