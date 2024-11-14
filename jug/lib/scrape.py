from jug.lib.logger import logger
# Making an HTTP Request
import requests
from bs4 import BeautifulSoup
import json


class Scrape():

    def __init__(self):
        self.result = None
        

    def getResult(self):
        return self.result


    def send_req(self, url):

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=6)
        response.encoding = "utf-8"

        # Cookies and sessions?
        # response = requests.Session()

        # cookies = response.cookies
          # Get the cookies from the response
        # response = requests.get(url, cookies=cookies, headers=headers)
          # Include the cookies in subsequent requests

        # Extract and process the data from the response
        # data = response.json()   # json
        # html = response.text     # html text
        # html = response.content  # binary
        # print(html)

        return response

    ###
      # def get_news(self):

      #     # logger.info(f'Yahoo reqs: {response.text}')
      #     # "Amazon, fiction, https://www.amazon.com/charts/mostsold/fiction/",
      #     # "Amazon, nonfiction, https://www.amazon.com/charts/mostsold/nonfiction/",

      #     url = "https://www.amazon.com/charts/mostsold/fiction/"
      #     base_url = "https://www.amazon.com"

      #     response = self.send_req(url)

      #     html = response.text

      #     linkList = []
      #     headlineList = []
      #     html_start = 0
      #     yy = 0
      #     num_results = 6   # number of results to get back

      #     for _ in range(num_results):

      #         html = html[html_start+yy:]
      #         html_start = html.find("data-ylk=\"itc:0;elm:hdln;elmt:")
      #         html_end = html_start + 2000
      #           # 2000 is an arbitrary number; to capture the section but not too big;

      #         if html_start < 0:
      #             break

      #         section = html[html_start:html_end]

      #         xx = section.find("href=")
      #         section = section[xx+6:]
      #         xx = section.find(">")

      #         link = section[:xx-1]
      #         if link.find("https://") == 0 and link.find(base_url) != 0:
      #             # Sometimes, randomly, gets strange sports ad and screws up the parsing;
      #             # But can't replicate it on demand; yahoo seems to insert it randomly;
      #             # Its base url is not yahoo.news but sports something;
      #             # print("bad news page")
      #             # print(html)
      #             self.get_news()
      #             break

      #         if link.find(base_url) != 0:
      #             link = base_url + link

      #         linkList.append(link)

      #         section = section[xx+1:]
      #         yy = section.find("<")


      #         headline = section[:yy]
      #         # decode html characters back to normal;
      #         # But this also seems to make headilne into type Beautifulsoup
      #         # So have to convert back to text, or else get error when trying to jsonify later;
      #         headline = BeautifulSoup(headline, "html.parser")
      #         headlineList.append(headline.text)

      #     # print(headlineList)
      #     # print(linkList)

      #     soup2 = []
      #     for idx in range(len(headlineList)):
      #         soup2.append([headlineList[idx], linkList[idx]])

      #     self.result = soup2

      # def get_britannica(self, location):

      #     # location = "Miami"

      #     url = 'https://www.britannica.com/search?query='
      #     response = self.send_req(f'{url}{location}')

      #     soup = BeautifulSoup(response.text, 'html.parser')


      #     # Find the specific script tag
      #     script_tag = soup.find('script', {'data-type': 'Init Mendel'})

      #     if not script_tag:
      #         logger.info(f'britannica not found: {location}')
      #         return False

      #     json_result = {}

      #     try:

      #         resultStart = script_tag.text.find("topicInfo")
      #         resultStart += 11

      #         resultEnd = script_tag.text.find("toc", resultStart)
      #         resultEnd -= 2

      #         result = script_tag.text[resultStart:resultEnd]

      #         json_result = json.loads(result)
      #         self.result = json_result
      #         # return json_result

      #         # print(json_result["title"])
      #         # print(json_result["url"])
      #         # print(json_result["description"])
      #         # print(json_result["imageUrl"])

      #     except Exception as e:
      #         logger.info(f"Britannica error: {e}")
      #         self.result = {}

    def get_rank_amazon(self):

        base_url = "https://www.amazon.com"
        url_list = [
            "https://www.amazon.com/charts/mostsold/fiction/",
            "https://www.amazon.com/charts/mostsold/nonfiction/"
        ]

        # Extract and process the data from the response
        # data = response.json()   # json
        # html = response.text     # html text
        # html = response.content  # binary
        # print(html)

        rank_all = []
        category = "fiction"

        # response_list = []
        rank = []
        for url in url_list:
            response = self.send_req(url)

            soup = BeautifulSoup(response.text, 'html.parser')
              # returns parsed HTML and creates a BeautifulSoup object


            lines = soup.find_all("a", class_="kc-cover-link app-specific-display not_app")[:20]
              # Get just 20; Amazon seems to repeat the list twice;

            # lines = soup.find("a", class_="kc-cover-link app-specific-display not_app")

            # rank = []
            rank_num = 0
            for line in lines:
                rank_num += 1
                url = line["href"]
                img_tag = line.find('img')
                img_src = img_tag["src"]
                title1 = img_tag["title"]
                  # title1 = "Cover image of The Five Year Lie by Sarina Bowen"
                # parse title1; get book title, author:
                title2 = title1.replace("Cover image of ", "")
                  # delete "Cover image of " string
                title3 = title2.split("by")
                  # split by "by"
                title = title3[0].strip()
                  # First half is the book title
                author = title3[1].strip()
                  # 2nd half is author

                # rank.append({
                #     "category" : category,
                #     "rank" : rank_num,
                #     "title" : title,
                #     "author": author,
                #     "amazonurl" : base_url + url,
                #     "imgurl" : img_src,
                # })
                row = (category,
                    rank_num,
                    title,
                    author,
                    base_url + url,
                    img_src
                )
                rank.append(row)

                # rank.append(category,
                #     rank_num,
                #     title,
                #     author,
                #     base_url + url,
                #     img_src
                # )


            # rank_all.append(rank)
            category = "nonfiction"

        self.result = rank
        # self.result = rank_all
        # This should result a list composed of 2 dictionaries:
          # rank_all = [
          #     {
          #         "category" : "fiction"
          #         ...
          #     },
          #     {
          #         "category" : "nonfiction"
          #         ...
          #     }
          # ]

        # How should this be called??
        # A rest call?
        # Calling a python script could be a pain because of the virtual environment;



    def doScrape(self):
        self.get_rank_amazon()





#----------------------------------------------

  # Find the specific script tag
  # script_tag = soup.find('script', {'data-type': 'Init Mendel'})

  # soup.find_all('a', {'class': 'kc-cover-link app-specific-display not_app'})[0]
  # print( soup.find_all('a', {'class': 'kc-cover-link app-specific-display not_app'}) )
  # print( soup.select('.kc-cover-link.app-specific-display.not_app') )
  # print( soup.find_all("a", class_="kc-cover-link app-specific-display not_app") )

  #----------------------------------------------

  # html = "<div><a href=\"https://hello.com\">hello text</a><img src=\"https://m.media-amazon.com/images/I/71WHWGojSJL.jpg\" alt=\"Cover image of The Boyfriend by Freida McFadden\" title=\"Cover image of The Boyfriend by Freida McFadden\" /></div>"

  # soup = BeautifulSoup(html, 'html.parser')
  # # f1 = soup.find('a', href=True)
  # f1 = soup.find('a')
  # print(f1)          # the whole a href line
  # print(f1["href"])  # get the url
  # print(f1.text)     # text only

  # f1 = soup.find('img')
  # print(f1)          # the whole a href line
  # print(f1["src"])   # get the url
  # print(f1["title"])   # get the url


  #----------------------------------------------

  # <a class="kc-cover-link app-specific-display not_app" href="/dp/B0CY337Q77/ref=chrt_bk_sd_fc_1_ci_lp">
  #     <img src="https://m.media-amazon.com/images/I/71WHWGojSJL.jpg" alt="Cover image of The Boyfriend by Freida McFadden" title="Cover image of The Boyfriend by Freida McFadden" />
  # </a>


  #     <div class="kc-rank-card-title">
  #         The Boyfriend
  #     </div>