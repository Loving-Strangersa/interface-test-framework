# -*- coding: utf-8 -*-
import allure

from KeywordDriven.step.step_movie import StepMovie
from KeywordDriven.step.step_movie_check import StepMovieCheck


class TestUser(StepMovie, StepMovieCheck):

    @allure.title("校验定位信息")
    def test_get_location_information(self):
        self.step_get_location_information({"headers": {"Applicationcode": "ZK231030975"}})
        self.step_check_location_information_list()

    def test_keyword_association(self):
        self.step_get_popular_searches()
        # self.step_keyword_association()
