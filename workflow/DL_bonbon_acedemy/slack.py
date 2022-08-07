import json
import requests
from loguru import logger


SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'


def send(text):
    global SLACK_HOOK_URL

    params = {
        'text': text,  # 通知内容
        'username': 'utadl',  # ユーザー名
    }

    data = json.dumps(params)
    ret = requests.post(SLACK_HOOK_URL, data=data)

    print(ret)


if __name__ == '__main__':
    send("Hello, world")

    from loguru import logger
    logger.add( send, level='INFO')
    logger.info('hello info')
    logger.debug('hello debug')