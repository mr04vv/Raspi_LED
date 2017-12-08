#!/usr/bin/python
# -*- coding: utf-8 -*-
# julitest0.py

import socket
import string
import led_h as on
import led_l as off

host = 'localhost'   # Raspberry PiのIPアドレス
port = 10500         # juliusの待ち受けポート

# パソコンからTCP/IPで、自分PCのjuliusサーバに接続
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

data = ""
while True:

    # "/RECOGOUT"を受信するまで、一回分の音声データを全部読み込む。
    while (string.find(data, "\n.") == -1):
        data = data + sock.recv(1024)

        # print(data)
        # data = ""
    # 音声XMLデータから、<WORD>を抽出して音声テキスト文に連結する。
    strTemp = ""
    for line in data.split('\n'):
        index = line.find('WORD="')
        idd = line.find('CLASSID="')

        if idd != -1:
            kkk = line[idd + 9:line.find('"', idd + 9)]
            if index != -1 and kkk != "3" and kkk != "4":
                line = line[index + 6:line.find('"', index + 6)]
                strTemp = strTemp + line

    # print("結果:" + strTemp)
    if strTemp == "ひかれごま":
        on.main()
    if strTemp == "うんこなう":
        off.main()
    # print(strTemp)
    data = ""
