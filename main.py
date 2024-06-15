from book_scraper import books_scraper,books_writer

# try the following:

def main():
  urls = [
  "http://books.toscrape.com/catalogue/category/books/classics_6/index.html",
  "http://books.toscrape.com/catalogue/category/books/horror_31/index.html",
  "http://books.toscrape.com/catalogue/category/books/history_32/index.html",
  "http://books.toscrape.com/catalogue/category/books/biography_36/index.html"
  ]   
  
  
  books_writer(urls)





if __name__ == '__main__':
  main()