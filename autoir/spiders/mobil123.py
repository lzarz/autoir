import datetime
import scrapy
from autoir.items import CarItem


class Mobil123Spider(scrapy.Spider):
    name = "mobil123"
    allowed_domains = ["mobil123.com"]
    start_urls = ["https://www.mobil123.com/mobil-bekas-dijual/indonesia"]

    @classmethod
    def update_settings(cls, settings):

        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        settings.set("FEEDS", {
            "data/%(name)s/" + current_time + ".csv": {
                "format": "csv",
                "encoding": "utf-8-sig",
                "fields": [
                    "title", "price"
                ],
            },
            "data/%(name)s/" + current_time + ".json": {
                "format": "json",
                "encoding": "utf-8",
            },
            "data/%(name)s/" + current_time + ".xml": {
                "format": "xml"
            }
        })

    def parse(self, response, **kwargs):

        cars = response.css("article.listing")

        for car in cars:
            car_item = CarItem()
            car_item["title"] = car.css("h2.listing__title.epsilon.flush > a::text").get().strip()
            car_item["price"] = car.css("div.listing__price::text").get()
            yield car_item
