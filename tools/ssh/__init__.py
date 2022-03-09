import paramiko
from public.handler_yaml import YamlClient
from abs_path import config_path


class SSLClient(object):

    def __init__(self, hostname=None, username=None, password=None, port=22):
        data = YamlClient.read_yaml(config_path)["ssh"]
        self.config = {
            "hostname": hostname or data["hostname"],
            "username": username or data["username"],
            "password": password or data["password"],
            "port": port or data["port"]
        }
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(**self.config)
        except paramiko.ssh_exception.SSHException as e:
            raise ValueError(f"连接服务器失败：{e}，massage：{self.config}")

    def execute(self, command: str):
        """
        执行ssh
        :param command: ssh命令
        :type command: str
        :return: 执行ssh命令返回的结果
        :rtype: str
        """
        stdin, stdout, stderr = self.client.exec_command(command)
        self.client.close()
        return stdout.read().decode('utf-8')

    def upload_file(self, local_path: str, remote_path: str):
        """
        上传文件到服务器
        :param local_path:本地文件目录
        :type local_path:str
        :param remote_path:服务器文件目录
        :type remote_path:str
        :return:
        :rtype:
        """
        connect_info = self.config
        tran = paramiko.Transport(connect_info["hostname"], connect_info["port"])
        tran.connect(username=connect_info["username"], password=connect_info["password"])
        sftp = paramiko.SFTPClient.from_transport(tran)
        sftp.put(local_path, remote_path)
        tran.close()

    def read_server_file(self, file_path: str):
        """
        读取服务器文件
        :param file_path:
        :type file_path:
        :return:
        :rtype:
        """
        sftp_client = self.client.open_sftp()
        remote_file = sftp_client.open(file_path)
        try:
            for line in remote_file:
                print(line)
        finally:
            remote_file.close()

    def download_file(self, local_path: str, remote_path: str):
        """
        下載文件到本地
        :param local_path:本地文件目录
        :type local_path:str
        :param remote_path:服务器文件目录
        :type remote_path:str
        :return:
        :rtype:
        """
        tran = self.client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(tran)
        sftp.get(remote_path, local_path)
        self.client.close()


if __name__ == '__main__':
    s = SSLClient()
    print(s.execute("ls"))
