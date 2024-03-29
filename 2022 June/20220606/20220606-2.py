from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1.創建套接字對象並指定使用哪種傳輸服務
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.綁定IP地址和端口(端口用於區分不同的服務)
    # 同一時間在同一個端口上只能綁定一個服務否則報錯
    server.bind(('192.168.1.2', 6789))
    # 3.開啟監聽 - 監聽客戶端連接到服務器
    # 參數512可以理解為連接隊列的大小
    server.listen(512)
    print('服務器啟動開始監聽...')
    while True:
        # 4.通過循環接收客戶端的連接並作出相應的處理(提供服務)
        # accept方法是一個阻塞方法如果沒有客戶端連接到服務器代碼不會向下執行
        # accept方法返回一個元組其中的第一個元素是客戶端對象
        # 第二個元素是連接到服務器的客戶端的地址(由IP和端口兩部分構成)
        client, addr = server.accept()
        print(str(addr) + '連接到了服務器.')
        # 5.發送數據
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.斷開連接
        client.close()


if __name__ == '__main__':
    main()