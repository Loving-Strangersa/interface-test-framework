import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v',
                 "--alluredir", "./allure-results",
                 # "-m hsf"
                 ])

os.system(r"allure generate --clean allure-results -o allure-report")
os.system(r"allure serve  allure-results")