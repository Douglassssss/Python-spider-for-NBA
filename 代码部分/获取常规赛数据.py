import requests
import json
import time

# 通过循环遍历每一个赛季的网址
# 这里注意，网页源代码里并没有所需数据，需通过抓包工具F12得到json文件
for year in range(1996, 2021):
    url = 'https://china.nba.com/static/data/league/playerstats_' \
          'All_All_All_0_All_false_{}_2_All_Team_points_All_total.json'.format(year)
    resp = requests.get(url)
    # 这里将得到的json文件转换为Python可以处理的字典
    dic = json.loads(resp.text)
    # 这里用的ANSI编码，目的是为了防止转换成Excel时出现乱码
    f = open(str(year) + '常规赛nba得分数据.txt', 'a+', encoding='ANSI')
    # 这里是遍历每个球员的数据，通过研究字典键值的规律
    for i in range(50):
        f.write(dic['payload']['players'][i]['playerProfile']['displayName'] + ','
                + str(dic['payload']['players'][i]["statTotal"]['points']) + '\n')
    time.sleep(0.5)   # 防止爬虫被封
    print('over!')    # 用于提示
    resp.close()
    f.close()
