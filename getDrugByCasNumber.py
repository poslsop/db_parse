import csv
import requests
from lxml import etree

# 将DrugBank中的cas-number放入该列表中
li = []
with open('(drugbank)target_drug_new.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for i in reader:
        # print(i[-1])
        if i[-1] in li:
            pass
        else:
            li.append(i[-1])
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=A4D102353C6E3D1D9BE691FCEBB5B25B; _ga=GA1.2.706958366.1618125049; cc_cookie_accept=cc_cookie_accept; _gid=GA1.2.1454560624.1620617175; JSESSIONID=D6354614D0E6B1EE135C2302118278BE; NSC_JOvskcx1eblbckadbl4r2pcq4hhqnel=ffffffff82df142045525d5f4f58455e445a4a423660; _gat=1',
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

f = open("CasNumber_GuidetoDrugName.csv", "a", newline='', encoding="utf-8")
csv_writer = csv.writer(f)
csv_writer.writerow(['CasNumber', 'GuidetoDrugName'])

length = len(li)
print(length)
for i in range(0, length):
    url = "https://www.guidetopharmacology.org/GRAC/DatabaseSearchForward?searchString=%s&searchCategories=all&species=none&type=all&comments=includeComments&order=rank&submit=Search+Database" % li[i]
    print(i)
    res = requests.get(url, headers = headers)

    if res.status_code == 200:
        tree = etree.HTML(res.text)
        drug_name = '-'
        try:
            drug_name = tree.xpath('/html/body/div/div[3]/div[2]/div/div/div[2]/b/a/text()')[0]
            cas_no = tree.xpath('/html/body/div/div[3]/div[2]/div/div/div[2]/div/text()')[0].replace('CAS Reg No.: ','')
            if cas_no == li[i]:
                csv_writer.writerow([li[i], drug_name])
        except:
            error = tree.xpath('/html/body/div/div[3]/div[2]/div/div/p[1]/text()')[0]
        f.flush()
f.close()