import csv
import requests
from lxml import etree
import re

# 将DrugBank中的cas-number放入该列表中
li = []
with open('(drugbank)target_drug_new.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for red in reader:
        if red[2] in li:
            pass
        else:
            li.append(red[2])
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=96D117639E7BBAD99E4252D6CDB23DBF; _ga=GA1.2.706958366.1618125049; cc_cookie_accept=cc_cookie_accept; JSESSIONID=B6C3E9E90A24990F06E550E51DABF901; NSC_JOvskcx1eblbckadbl4r2pcq4hhqnel=ffffffff82df142045525d5f4f58455e445a4a423660; _gid=GA1.2.1078056230.1622184099; _gat=1',
        'Host': 'www.guidetopharmacology.org',
        'Referer': 'https://www.guidetopharmacology.org/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}

f = open("compare/drugbank_drugID2guideto_drugID.csv", "a", newline='', encoding="utf-8")
csv_writer = csv.writer(f)
csv_writer.writerow(['drugbank_drugID', 'guideto_drug_id'])

length = len(li)
print(length)
for i in range(5097, length):
    url = "https://www.guidetopharmacology.org/GRAC/DatabaseSearchForward?searchString=%s&searchCategories=all&species=none&type=all&comments=includeComments&order=rank&submit=Search+Database" % li[i]
    print(i)
    res = requests.get(url, headers = headers)

    if res.status_code == 200:
        tree = etree.HTML(res.text)
        drug_url = '-'
        try:
            drug_url = tree.xpath('/html/body/div/div[3]/div[2]/div/div/div[2]/b/a/@href')[0]
            print(drug_url)
            drug_id = re.findall('\d+', drug_url)[0]
            csv_writer.writerow([li[i], drug_id])
        except:
            error = tree.xpath('/html/body/div/div[3]/div[2]/div/div/p[1]/text()')[0]
        f.flush()
f.close()
