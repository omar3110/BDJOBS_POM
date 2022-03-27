from Pages.home_page import Resourses as R
from seleniumbase import BaseCase


class HomeTest(BaseCase):
    def test_home_page(self):

        self.open(R.URL)

        self.assert_title(R.Title)
        self.assert_element(R.logo)
        self.click(R.SignIn)
        self.sleep(5)
        self.click(R.MyJobsSignIn)
        self.sleep(5)
        self.type(R.username_selector, R.username)
        self.sleep(2)
        self.click(R.next_button)
        self.sleep(2)
        self.type(R.password_selector, R.password)
        self.sleep(2)
        self.click(R.login_button)
        self.sleep(5)
        self.type(
            '/html/body/div[11]/div/div/div[1]/div/div[1]/form/div[1]/input', 'IT')
        self.sleep(2)
        self.click(
            '/html/body/div[11]/div/div/div[1]/div/div[1]/form/div[2]/select')
        self.sleep(5)
        self.click(
            '/html/body/div[11]/div/div/div[1]/div/div[1]/form/div[2]/select/option[5]')
        self.sleep(5)
        self.click(
            '/html/body/div[11]/div/div/div[1]/div/div[1]/form/input[2]')
        self.sleep(10)
