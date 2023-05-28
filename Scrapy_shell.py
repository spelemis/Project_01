# Собрать информацию об авторах и книгах
# TODO - scrapy shell: найти правильный xml-путь
 
import scrapy
 
class LitresSpider(scrapy.Spider):
    name = 'litres_crawler'
    start_urls = ['https://www.litres.ru/genre/knigi-detektivy-5022/']
 
    def parse(self, response):
        for card in response.xpath('//*[@id="__next"]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div/div[1]'):
            name = card.xpath('//*[@div]').get()
            author = card.xpath('//*[@div]').get()
 
        yield {
            "Author": author,
            "Name": name,
        }
