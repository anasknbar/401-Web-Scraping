# 401-Web-Scraping

### this web scraper project consist of two functions: 

1- the **"books_scraper"** function  
- which is resposible for scraping the data from the website 

2- the **"books_writer"** functin  
- which is resposible for making the json file that contains the scraped book data

both the functions are in the 'book_scraper.py' file

### how the program works ??

all you have to do is feeding the **"books_writer"** function with a list of categories url from the 
**"Books to Scrape"** website.
the function will scrap each category page and write them into a json file.

### example:

    # list of urls for classics,horror,history,and biography pages 

    urls = [
    "http://books.toscrape.com/catalogue/category/books/classics_6/index.html",
      "http://books.toscrape.com/catalogue/category/books/horror_31/index.html",
      "http://books.toscrape.com/catalogue/category/books/history_32/index.html",
      "http://books.toscrape.com/catalogue/category/books/biography_36/index.html"
      ]  

    # calling the books_writer function
    books_writer(urls)
 

