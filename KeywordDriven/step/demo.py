from KeywordDriven.ApiHandle.apihandle import DataHandle


class StepApiClient(DataHandle):
    def step_inquiry_of_id_card(self, yal_data):

        """TODO:暂时省略获取yaml存取的参数,并返回数据"""
        self.inquiry_of_id_card_pp(params=yal_data)
