import random
import string

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

    # @staticmethod
    # def get_time(length=None):
    #     """
    #     获取时间戳
    #     :return:
    #     :rtype:
    #     """
    #     return time.time() * 1000[:length] if length else time.time() * 1000

    @staticmethod
    def generate_random_string(length=None, min_length=None, max_length=None):
        """
        生成随机字符串。

        :param length: 如果提供，则生成长度为length的随机字符串。
        :param min_length: 最小长度，与max_length一起使用时，生成长度为[min_length, max_length]区间的随机字符串。
        :param max_length: 最大长度，与min_length一起使用时，生成长度为[min_length, max_length]区间的随机字符串。
        :return: 生成的随机字符串。
        """
        if length is not None:
            # 如果只提供了length，则生成对应长度的字符串
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        elif min_length is not None and max_length is not None:
            # 如果提供了min_length和max_length，则生成随机区间长度的字符串
            if min_length > max_length:
                raise ValueError("min_length cannot be greater than max_length")
            length = random.randint(min_length, max_length)
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        else:
            # 如果没有提供任何参数或参数无效，则抛出一个异常或返回一个默认字符串
            raise ValueError("Either 'length' or both 'min_length' and 'max_length' must be provided.")

    @property
    def random_bool(self):
        """
        随机返回bool
        :return:
        :rtype:
        """
        return random.choice([True, False])


faker = RandomData()

if __name__ == '__main__':
    # print(faker.get_time(6))
    print(faker.generate_random_string(min_length=1, max_length=32))
    print(faker.random_bool)
