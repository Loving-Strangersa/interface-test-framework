import os

# 项目根目录
import time

dir_path = os.path.dirname(os.path.abspath(__file__))

# 配置yaml文件
config_path = os.path.join(dir_path, "config", "config.yaml")

# 日志文件
log_path = os.path.join(dir_path, "log")

# 本地时间戳
time_now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
