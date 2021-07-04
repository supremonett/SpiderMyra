from scrapy.http.request.form import FormRequest
import scrapy
from SpiderMyra.items import SpidermyraItem


class MyraSpider(scrapy.Spider):
    name = 'myra'
    url = 'http://quotes.toscrape.com'

    def start_requests(self):
        urls = [
            self.url+'/login',
            self.url+'/page/1/',
        ]
        cont = 0
        for url in urls:
            if(cont == 0):
                print('------------ Logando no Site --------------')
                yield scrapy.Request(url=urls[cont], callback=self.parse)
            else:
                yield scrapy.Request(url=urls[cont], callback=self.coletarDados)
            cont += 1

    def parse(self, response):
        token = response.xpath('//div[@class="row header-box"]/a/@href').get()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'supremonett@gmail.com',
            'password': '1234',
        })


    def coletarDados(self, response):
        print('---------- Coletando Quotes -------------')
        item = SpidermyraItem()
        for i in response.xpath('//div[@class="quote"]'):
            item['texto'] = i.xpath('.//span[@class="text"]/text()').get(),
            item['autor'] = i.xpath('.//small[@class="author"]/text()').get(),
            item['tags'] = i.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            yield item
            
        proximaPg = response.xpath('//a[contains(text(),"Next ")]//@href').get()
        if proximaPg:
            proximaP = self.url+proximaPg
            yield scrapy.Request(url=proximaP, callback=self.coletarDados)