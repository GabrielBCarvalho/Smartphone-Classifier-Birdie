import scrapy

class SmartphonesSubmarinoSpider(scrapy.Spider):
    name = "submarino"
    submarino_url = "https://www.submarino.com.br"
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    register_counters = 0

    
    def start_requests(self):
        urls = [
            'https://www.submarino.com.br/categoria/celulares-e-smartphones/smartphone?ordenacao=relevance'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers = self.headers)


    def parse(self, response):
        if(self.register_counters < 2600):
            for smartphone in response.css("div.product-grid-item.ColUI-sc-1ey7nd2-0.fDxHZn.ViewUI-oocyw8-6.kvewNe"):
                print(self.register_counters)
                yield{
                    'title': smartphone.css('h3.TitleUI-sc-1m3ayw0-17.eefpzi.TitleH3-c6mv26-2.YHJwU::text').get(),
                    'url': self.submarino_url + smartphone.css('a.Link-sc-1m3ayw0-2.dzqrLh.TouchableA-sc-9v9alh-0.cXaYNF::attr(href)').get()
                }
                self.register_counters += 1

            next_page = response.xpath('/html/body/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div/div/div[2]/div/ul/li[10]/a/@href').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback = self.parse, headers = self.headers)