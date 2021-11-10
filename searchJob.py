import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

payload = '''ro: 0
kwop: 7
keyword: 資料工程師
expansionType: area,spec,com,job,wf,wktm
order: 15
asc: 0
page: 2
mode: s
jobsource: 2018indexpoc
langFlag: 0'''
payload = {p.split(': ')[0]: p.split(': ')[1] for p in payload.split('\n')}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
outurl = 'https://www.104.com.tw/jobs/search/?'
payload['keyword'] = '資料工程師'
payload['page'] = '1'

res = requests.get(outurl, headers=headers, params=payload)
soup = BeautifulSoup(res.text, 'html.parser')
df = pd.DataFrame(columns=['公司', '職位', '地點', '內容', '薪水', '網址', '所需工具', '技能', '其他條件'])
resArticle = soup.select('div[id="js-job-content"]')

n = 0
for i in resArticle:
    for j in i.select('h2[class="b-tit"]'):
        print(j.a.text)
        print('https:' + j.a['href'])
        url = 'https:' + j.a['href']
        inurl = url.replace("www", "m")
        res = requests.get(inurl, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        title = soup.select('h1[class="title"]')[0].text
        company = soup.select('h2[class="company"]')[0].text
        loc = soup.select('td')[0].a.text.strip('\n').strip(' ')
        content = soup.select('div[class="content"]')[1].text.strip('\n').strip(' ')
        salary = soup.select('div[class="content"]')[2].td.text.strip('\n').strip(' ').replace(' ', '').split('\n')[0]
        title_url = soup.select('h2[class="company"]')[0].a['href']
        my_dict = {}
        for tab in soup.select('div[class="content"]')[5].select('table'):
            for n in range(len(tab.select('th'))):
                my_dict[tab.select('th')[n].text.split('：')[0]] = tab.select('td')[n].text.strip('\n').strip(' ')
        try:
            tool = my_dict['擅長工具']
            prefer = my_dict['工作技能']
            others = my_dict['其他條件']
        except:
            None

        datas = [title, company, loc, content, salary, title_url, tool, prefer, others]
        df.loc[n] = datas
        time.sleep(5)
        n += 1

df.to_csv('./re104.csv')

