import requests
import time
url = 'https://store.steampowered.com/appreviews/1049100?json=1'
params = {'filter': 'recent', 'language': 'all', 'cursor': '*', 'purchase_type': 'all', 'num_per_page': 100}
urljson = requests.get(url, params=params)
print('URL地址：', urljson.url)
fh = open('steam_review.txt','w',encoding='utf-8')
data = urljson.json()  # 如响应是json数据 ，可以使用 r.json()自动转换为dict
while data['success'] == 1:
    for review in data['reviews']:
        fh.write('steamid ' + review['author']['steamid'] +'\n' )
        fh.write('游戏时长 ' + str(review['author']['playtime_forever']) + '\n')
        t = time.gmtime(review['timestamp_created'])
        fh.write('评论时间 ' + str(t[0]) + '年' + str(t[1]) + '月' + str(t[2]) + '日' + str(t[3]) + '时'+ str(t[4]) + '分' + str(t[5]) + '秒' + '星期' + str(t[6]) + '\n')
        fh.write(review['review'] + '\n')
    params['cursor'] = data['cursor']
    urljson = requests.get(url, params=params)
    print('URL地址：', urljson.url)
    data = urljson.json()
fh.close()