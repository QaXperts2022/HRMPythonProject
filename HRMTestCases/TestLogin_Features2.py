import pytest
import self

from conftest import *
from HRMPages.LoginPage import LoginPage
@pytest.mark.usefixtures("browser_setup")
class LoginPage:

    def __init__(self):
        self.login_page = None
        self.driver = None

    self.driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
         self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
         self.login_page.login(Username, Password)

    def teardown_class(self):
         self.driver.quit()