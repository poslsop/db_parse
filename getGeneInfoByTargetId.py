import requests

def getTargetIds(headers):
    target_id_url = "https://www.guidetopharmacology.org/services/targets"
    taget_ids = requests.get(url=target_id_url, headers = headers).json()
    for i in taget_ids:
        taget_id = i["targetId"]
        getGeneByTargetId(taget_id, headers)

def getGeneByTargetId(target_id, headers):
    gene_url = "https://www.guidetopharmacology.org/services/targets/%s/geneProteinInformation"%target_id
    gene_url_data = requests.get(gene_url, headers=headers)

    gene_name_list = []
    if gene_url_data.status_code == 200:
        ligand_data = gene_url_data.json()
        for i in ligand_data:
            gene_name = i["geneName"]
            if gene_name in gene_name_list:
                pass
            else:
                gene_name_list.append(gene_name)
                print(gene_name_list)
    return gene_name_list


if __name__ == "__main__":
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.706958366.1618125049; cc_cookie_accept=cc_cookie_accept; _gid=GA1.2.1454560624.1620617175; NSC_JOvskcx1eblbckadbl4r2pcq4hhqnel=ffffffff82df142045525d5f4f58455e445a4a423660',
        'Host': 'www.guidetopharmacology.org',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    }
    getTargetIds(headers)