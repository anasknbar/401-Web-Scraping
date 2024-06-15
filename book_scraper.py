from bs4 import BeautifulSoup
import requests
from word2number import w2n
import json

def books_scraper(url:str):
  
  
    # send request for the wanted page
    html_text = requests.get(url).text
    # make an instance of the soup library
    soup = BeautifulSoup(html_text,'lxml')
    
    
    
    genre = soup.find('div',class_='page-header action').h1.text
    books_list = {  
                    "type":genre,
                    "data":[]
                }
    
    books = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
 
    for index,book in enumerate(books):
      
      title = book.find('h3').text
      rating = book.find('p',class_='star-rating')['class'][1]
      price = book.find('p',class_='price_color').text[2:]
      availability = book.find('p','availability').text.strip()

      books_list["data"].append(
      {
        "title":title,
        "rating":f"{w2n.word_to_num(rating)}/5",
        "price":f"${price}",
        "availability":availability
      })
    return books_list
      # with open(f'{genre}.json','w') as file:
      #   books_json = json.dumps(books_list,indent=4)
      #   file.write(f"{books_json}")
 
 



def books_writer(urls:list):
  api_book_list = []
  for url in urls:
      api_book_list.append(books_scraper(url))
  with open('book_api.json','w') as file:
    books_json = json.dumps(api_book_list,indent=4)
    file.write(f"{books_json}")
    

    
    

    





