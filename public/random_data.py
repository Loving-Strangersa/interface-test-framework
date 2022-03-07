from faker import Faker


class RandomData(object):

    def __init__(self):
        self.faker = Faker(locale='zh_CN')

    def random_user_agent(self):
        """
        随机生成请求头
        :return:
        :rtype:
        """
        return self.faker.user_agent()

    def random_phone(self):
        """
        随机生成电话号码
        :return:
        :rtype:
        """
        return self.faker.phone_number()

    def random_name(self):
        """
        随机生成姓名
        :return:
        :rtype:
        """
        return self.faker.name()

    def random_email(self):
        """
        随机生成邮箱地址
        :return:
        :rtype:
        """
        return self.faker.free_email()


counterfeit = RandomData()
