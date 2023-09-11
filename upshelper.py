import socket
import time
import os

print("作者：Angel_group")
print("未经允许，禁止转载")
print("此版本为测试版，不带表最终作品")
print("原理：检测网络状态，断电后网络未连接，执行关机命令，保护硬盘")
print("#########################")
print("开始检测")
print("#########################")
while True:
    def test_connect(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((host, port))
            print('未断电')
            os.system("shutdown -a")
        except socket.error as e:
            print('检测到断电，即将在60秒后关机')
            os.system("shutdown -s -t  60 ")
        finally:
            s.close()
    if __name__ == '__main__':
    # 测试连接
        test_connect('www.baidu.com', 80)

    print("继续监控ups状态")
    print("#########################")
    time.sleep(60)  # 暂停60秒钟