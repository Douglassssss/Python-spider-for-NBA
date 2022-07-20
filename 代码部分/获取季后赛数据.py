import requests
import json
import time

# 代码原理同获取常规赛数据
for year in range(2005, 2021):
    url = 'https://china.nba.com/static/data/league/playerstats_' \
          'All_All_All_0_All_false_{}_4_All_Team_points_All_total.json'.format(year)
    resp = requests.get(url)
    dic = json.loads(resp.text)
    f = open(str(year) + '季后赛nba得分数据.txt', 'a+', encoding='utf-8')
    for i in range(50):
        f.write(dic['payload']['players'][i]['playerProfile']['displayName'] + ','
                + str(dic['payload']['players'][i]["statTotal"]['points']) + '\n')
        time.sleep(0.5)
    resp.close()
    f.close()
