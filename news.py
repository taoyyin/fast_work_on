if __name__ == '__main__':
    import requests

    headers = {
        "authority": "bbsapi.masutaa.com",
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://bbs.masutaa.com",
        "referer": "https://bbs.masutaa.com/",
        "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    url = "https://bbsapi.masutaa.com/queryTopicList"
    params = {
        "tagId": "41527586985921",
        "page": "2",
        "essence": "false"
    }
    response = requests.get(url, headers=headers, params=params).json()
    text = ""
    for res in response['records']:
        text = text + res["title"]+';'
    print(text)