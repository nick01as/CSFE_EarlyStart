import requests
from bs4 import BeautifulSoup

class event():
    def __init__(self, title, date, duration, descrip, img, url):
        self.title = title
        self.date = date
        self.duration = duration
        self.descrip = descrip
        self.img = img
        self.url = url

if __name__ == '__main__':
    URL = "https://calendar.ucsd.edu/pages/upcoming-events"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="cal-content")
    events = results.find_all("div", class_ = "teaser-content clearfix")

    allEvents = []

    for e in events:
        title = e.find("h2").text.strip()

        date = (e.find("span", class_ = "startDate").text.strip(), 
                e.find("span", class_ = "endDate").text.strip())
        
        duration = e.find("span", class_ = "endDate").next_sibling.text.strip()
        duration = duration.replace("from ","")
        duration = duration.replace("(","").replace(")","")

        descrip = e.find("p").text.strip()

        img = e.find("img")["src"].strip()

        url = e.find("a")["href"].strip()

        allEvents.append(event(title = title,
                               date = date,
                               duration = duration,
                               descrip = descrip,
                               img = img,
                               url = url))
        
