import random
import string
import time

from faker import Faker


class RandomData(object):

    def __init__(self):
        self.faker = Faker(locale='zh_CN')

    @property
    def random_user_agent(self):
        """
        随机生成请求头
        :return:
        :rtype:
        """
        return self.faker.user_agent()

    @property
    def random_phone(self):
        """
        随机生成电话号码
        :return:
        :rtype:
        """
        return self.faker.phone_number()

    @property
    def random_name(self):
        """
        随机生成中文姓名
        :return:
        :rtype:
        """
        return self.faker.name()

    @property
    def random_email(self):
        """
        随机生成邮箱地址
        :return:
        :rtype:
        """
        return self.faker.free_email()

    @property
    def random_username(self):
        """
        随机生成英文+数字用户名1-4位
        :return:
        :rtype:
        """
        return string.hexdigits[0:random.randint(2, 4)]

    @property
    def random_password(self):
        """
          随机生成英文+数字密码6-12
        :return:
        :rtype:
        """
        return "".join([random.choice(string.hexdigits) for _ in range(6, 12)])

    @staticmethod
    def get_time(length=None):
        """
        获取时间戳
        :return:
        :rtype:
        """
        return time.time() * 1000[:length] if length else time.time() * 1000


faker = RandomData()

if __name__ == '__main__':
    print(faker.get_time(6))
