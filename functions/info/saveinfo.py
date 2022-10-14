#!/bin/python3
import json

import requests
from bs4 import BeautifulSoup
from lxml import etree

HEADERS = {
"Host": "www.beecrowd.com.br",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "pt-BR,pt;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Content-Type": "text/html; charset=utf-8",
"Alt-Used": "www.beecrowd.com.br",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"TE": "trailers"
}

class GetInfo:
    def __init__(self, number: str):
        self.number = number
        self.link = f"https://www.beecrowd.com.br/judge/pt/problems/view/{number}"

    def get_text(self):
        response = requests.get(f"https://www.beecrowd.com.br/repository/UOJ_{self.number}.html", headers=HEADERS)
        response.encoding = response.apparent_encoding
        return response.text

    def parse_content(self, content):
        atributes = {}
        
        soup = BeautifulSoup(content, 'html.parser')
        dom = etree.HTML(str(soup))
        
        """ HEADER """
        atributes["link"] = self.link
        atributes["title"] = soup.title.string
        atributes["author"] = dom.xpath('/html/body/div[1]/div/p')[0].text.strip()
        
        """ TIMELIMIT """
        all_text = soup.get_text().split("\n")
        for line in all_text:
            if "Timelimit" in line:
                atributes["timelimit"] = line.replace("Timelimit: ", "")
                break
        
        """ DESCRIPTION """
        atributes["description"] = self.__getContentByClass__("description", soup)

        """ INPUT """
        atributes["input"] = self.__getContentByClass__("input", soup)

        """ OUTPUT """
        atributes["output"] = self.__getContentByClass__("output", soup)

        """ INPUT VALUES """
        atributes["input-example"] = self.__getContentByClass__("division", soup, header="td")
        
        """ OUTPUT VALUES """
        atributes["output-example"] = soup.find_all("td")[3].get_text()

        return atributes

    def write_in_file(self, atributes_dict):
        jsonify = json.dumps(atributes_dict, indent=4)
        with open(f"repo/info/{self.number}.json", "w") as file:
            file.write(jsonify)

        return f"repo/info/{self.number}.json"


    def __getContentByClass__(self, nameclass, soup, header="div"):
        content = str(soup.find_all(header, class_ = nameclass))
        content = content.replace("]", "").replace("[", "")
        soup_content = BeautifulSoup(content, 'html.parser')
        return soup_content.get_text()

