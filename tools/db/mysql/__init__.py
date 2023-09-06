import pymysql

from abs_path import config_path
from public.handler_yaml import YamlClient
from public.log import Log


class MySQLClient(object):

    def __init__(self, host=None, database=None, password=None, user="root", port=3306):
        """

        :param host: 数据库地址
        :type host: str
        :param configbase: 数据库库名
        :type configbase: str
        :param user: 登录名称
        :type user: str
        :param password: 登录密码
        :type password: srt
        :param port: 数据库开放端口号
        :type port: number
        """
        config = YamlClient.read_yaml(config_path)["mysql"]

        self.config = {
            "host": host or config["host"],
            "port": port or config["port"],
            "user": user or config["user"],
            "passwd": password or config["password"],
            "database": database or config["database"],
            "charset": "utf8mb4",
            "cursorclass": config.get("is_dict") or pymysql.cursors.DictCursor
        }
        Log.info("连接MySQL信息:{}".format(self.config))
        self.connect = pymysql.connect(
            **self.config
        )

        self.cur = self.connect.cursor()

    def execute(self, sql: str):
        """
        执行sql
        :param sql: 要执行的sql语句
        :type sql: str
        :return: 数据库查询结果
        :rtype: list[dict]
        """
        self.connect.commit()
        self.cur.execute(sql)
        response = self.cur.fetchall()
        self.close()
        return response

    def close(self):
        self.cur.close()
        self.connect.close()


if __name__ == '__main__':
    a = MySQLClient("47.107.45.202")
    # print(    sql.execute("show databases"))
    # print(sql.execute("show tables"))
    print(a.execute("select * from db"))
