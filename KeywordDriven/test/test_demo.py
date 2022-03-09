from KeywordDriven.step.demo import StepApiClient


class TestCase(StepApiClient):

    def test_inquiry_of_id_card(self):
        self.step_inquiry_of_id_card(
            {"username": "18574783294", "password": "nightfell.", "sessitime": "2022-02-28+17%3A50%3A00",
             "sessiond": "saas", "method": "login"})

        self.step_inquiry_of_id_card({"method": "detailed2", "id": "234266219"})


if __name__ == '__main__':
    a = TestCase()
    a.test_inquiry_of_id_card()
