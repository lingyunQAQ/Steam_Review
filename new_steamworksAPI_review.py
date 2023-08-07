import random

import requests
import pandas as pd
import time
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-CN '
}
def run(game_id):
    """
    从Steam获取最新评论数据并保存到表格中
    """
    url = f'https://store.steampowered.com/appreviews/{game_id}?json=1'
    # 拼接URL
    params = {'filter': 'recent', 'language': 'all', 'cursor': '*', 'purchase_type': 'all', 'num_per_page': 100}
    url_json = requests.get(url, params=params,headers=headers)
    print('The current URL：', url_json.url)

    # 创建一个列表来存储评论数据
    review_data = []
    # 提取数据
    data = url_json.json()
    while data['reviews']: # 开冲！
        for review in data['reviews']:
            review_entry = {
                'SteamID': review['author']['steamid'],
                '游戏时长（小时）': review['author']['playtime_forever']
            }

            t = time.gmtime(review['timestamp_created'])

            review_entry['评论时间'] = f"{t[0]}年{t[1]}月{t[2]}日 {t[3]}时{t[4]}分{t[5]}秒 星期{t[6]}"
            review_entry['评论内容'] = review['review']
            review_data.append(review_entry)

        # 获取游标继续拼接下一页URL
        params['cursor'] = data['cursor']
        url_json = requests.get(url, params=params)
        print('The current URL：', url_json.url)
        data = url_json.json()

    # 将评论数据转换为DataFrame
    df = pd.DataFrame(review_data)

    # 将DataFrame保存为CSV表格
    df.to_csv(f'{game_id}.csv', index=False ,encoding='utf-8-sig')
    print("The data has been successfully saved to the table")


if __name__ == '__main__':
    game_id = input('game_id：')
    start_time = time.time()
    run(game_id=game_id)
    end_time = time.time()
    input(f"\n运行结束共用时{float(end_time-start_time)}秒，超越了{random.randint(1,100)}%的用户！真的是太快啦！\n回车结束运行！")
