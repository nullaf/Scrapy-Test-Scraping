# Webscraping using Scrapy

This is a Scrapy project to scrape mock book data's from [here](https://books.toscrape.com/)

## Requirements:

1. [Python 3](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/) (`pip3 install scrapy`)

## Extracted data

This project extracts titles, prices, ratings and urls of books.

The extracted data looks like this sample:

    {
        'title': 'A Light in the Attic',
        'price': '£51.77',
        'rating': 'Three',
        'link': 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    }

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl bookspider

If you want to save the scraped data to a file, you can pass the `-o` option:

    $ scrapy crawl bookspider -o books.json
    $ scrapy crawl bookspider -o books.csv