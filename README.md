pip install pyjwt

Запустите оба скрипта командами ```python LoggerServer.py``` и ```python TokenServer.py```

Введите команду ```nc localhost 8000``` и отправьте сообщение ```{"code": "your code"}```
В ответ получите токен
Введите команду ```nc localhost 8001``` и отправьте сообщение ```{"token": "token", "text": "your text"}```

Или воспользуйтесь клиентом client.py