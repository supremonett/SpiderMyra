from scrapy.http.request.form import FormRequest
import scrapy


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
        print('---------- COLETANDO DADOS -------------')
        for i in response.xpath('//div[@class="quote"]'):
            texto = i.xpath('.//span[@class="text"]/text()').get(),
            autor = i.xpath('.//small[@class="author"]/text()').get(),
            tags = i.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            print(tags)
