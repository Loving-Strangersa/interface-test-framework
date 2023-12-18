from KeywordDriven.ApiHandle.handle_movie import Movie


class MovieClient(Movie):

    def get_location_information(self, params):
        return self._get_location_information(params)

    def get_popular_searches(self, params):
        return self._get_popular_searches(params)

    def keyword_association(self, params):
        return self._keyword_association(params)
