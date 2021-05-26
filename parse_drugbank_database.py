import xml.etree.ElementTree as ET
import csv

tree = ET.parse('D:/毕设数据库/毕设数据库/DrugBank/drugbank_all_full_database/full database.xml')
drugs = tree.findall("drug")
# 获取靶点信息
f_targetInfo = open("(drugbank)targetInfo.csv", "w", newline='', encoding="utf-8")
f_targetInfo_csv_writer = csv.writer(f_targetInfo)
f_targetInfo_csv_writer.writerow(['target_id', 'target_name', 'target_type', 'general_function', 'gene_name', 'gene_sequence', 'source', 'url'])
for drug in drugs:
    targets = drug.find("targets").findall("target")
    for target in targets:
        target_name = target.find("name").text
        target_type = '-'
        try:
            target_type = target.find('actions').find('action').text
        except:
            pass
        polypeptide = target.find("polypeptide")
        general_function = '-'
        try:
            polypeptide.find('general-function').text
        except:
            pass
        gene_name = '-'
        try:
            gene_name = polypeptide.find("gene-name").text
        except:
            pass
        gene_sequence = '-'
        try:
            gene_sequence = polypeptide.find('gene-sequence').text
        except:
            pass
        target_id = '-'
        try:
            target_id = polypeptide.get("id")
        except:
            pass
        if target_id != '-':
            source = "DrugBank"
            url = 'https://go.drugbank.com/polypeptides/%s'%target_id
            f_targetInfo_csv_writer.writerow([target_id, target_name, target_type, general_function, gene_name, gene_sequence, source, url])
    f_targetInfo.flush()
f_targetInfo.close()

# 获取药物信息
f_targetDrugnfo = open("../../save2db/success/(drugbank)drug_info.csv", "w", newline='', encoding="utf-8")
f_targetDrugnfo_csv_writer = csv.writer(f_targetDrugnfo)
f_targetDrugnfo_csv_writer.writerow(['drug_id', 'drug_name',  'drug_type',  'is_approved', 'casnumber',  'product',  'food_interactions',  'description', 'source', 'url'])
for drug in drugs:
    food_interactions = '-'
    product = '-'
    description = '-'
    drug_id = drug.find('drugbank-id').text
    drug_name = drug.find("name").text
    drug_type = drug.get("type")
    is_approved = drug.find('groups').find("group").text
    cas_number = drug.find('cas-number').text
    source = "DrugBank"
    url = 'https://go.drugbank.com/drugs/%s'%drug_id
    try:
        product = drug.find('products').find('product').find('name').text
        food_interactions = drug.find('food-interactions').find('food-interaction').text
        description = drug.find('description').text.replace('\n', '')
    except:
        pass
    #print(drug_id, drug_name, drug_type, is_approved, cas_number, product, food_interactions, description, source, url)
    f_targetDrugnfo_csv_writer.writerow([drug_id, drug_name, drug_type, is_approved, cas_number, product, food_interactions, description, source, url])
    f_targetDrugnfo.flush()
f_targetDrugnfo.close()
