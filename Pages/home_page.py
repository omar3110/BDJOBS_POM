from seleniumbase import BaseCase


class Resourses():
    URL = "https://www.bdjobs.com/"
    Title = "Largest Job Site in Bangladesh, Search Jobs | Bdjobs.com"
    logo = "/html/body/header/div/div/div/nav/div[1]/a/img"
    SignIn = '/html/body/header/div/div/div/nav/div[2]/ul/li[3]/a'
    MyJobsSignIn = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/ul/li/div[1]/div[2]/div[3]/a[1]'
    username_selector = "/html/body/section/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/fieldset/label/input"
    username = 'omarfaruq3110@gmail.com'
    next_button = '/html/body/section/div/div/div/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/input'
    password_selector = '/html/body/section/div/div/div/div/div[2]/div/div[1]/form/div[2]/div/div[1]/fieldset/label/input'
    password = 'o01676787008'
    login_button = '/html/body/section/div/div/div/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
