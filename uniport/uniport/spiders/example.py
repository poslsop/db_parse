import scrapy
import csv

from test.uniport.uniport.items import UniportItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['uniport.org']
    #start_urls = ['http://uniport.org/']



    def start_requests(self):
        # url = "https://platform-api.opentargets.io/v3/platform/public/evidence/filter?size=10000&datasource=chembl&fields=access_level&fields=disease.efo_info&fields=drug.id&fields=drug.molecule_name&fields=drug.molecule_type&fields=target.activity&fields=target.gene_info&fields=target.target_class&fields=target.target_name&fields=target.target_type&target=ENSG00000157404&disease=EFO_0009690&expandefo=true"
        targets = {}    # key target_name, value  key
        with open('(guideto)target_drug.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for i in reader:
                targets[i[1]] = i[0]

        count = 0
        for target_name in targets:
            count += 1
            url = 'https://www.uniprot.org/uniprot/?query=%s&sort=score'%target_name

            print(str(count) + "------" + target_name +"--")
            yield scrapy.Request(url=url, meta={'guideto_target_id': targets[target_name]}, callback=self.parse)

    def parse(self, response):
        guideto_target_id = response.meta['guideto_target_id']
        item = UniportItem()
        if response.status == 200:
            drugbank_target_id = response.xpath('//form/table/tbody/tr[1]/td[2]/a/text()')[0].extract()
        else:
            drugbank_target_id = '-'
        item['guideto_target_id'] = guideto_target_id
        item['drugbank_target_id'] = drugbank_target_id
        yield item



