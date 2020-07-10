import re
import ast
import requests
from urllib import parse
from scrapy import Selector

domain="https://bbs.csdn.net"
def get_node_json():
    left_menu_text=requests.get("https://bbs.csdn.net/dynamic_js/left_menu.js?csdn").text
    nodes_str_match=re.search("forumNodes: (.*])",left_menu_text)
    if nodes_str_match:
        nodes_str=nodes_str_match.group(1).replace("null","None")
        nodes_list=ast.literal_eval(nodes_str)
        return nodes_list
    return []

url_list=[]
def process_nodes_list(nodes_list):
    #将json格式提取出url到list中
    for item in nodes_list:
        if "url" in item:
            if item["url"]:
                url_list.append(item["url"])
            if "children" in item:
                process_nodes_list(item["children"])

def get_level1_list(nodes_list):
    level1_url=[]
    for item in nodes_list:
        if "url" in item and item["url"]:
            level1_url.append(item["url"])

    return level1_url

def get_last_urls():
    #获取最终需要抓取的url
    nodes_list=get_node_json()
    process_nodes_list(nodes_list)
    level1_url=get_level1_list(nodes_list)
    last_urls=[]
    for url in url_list:
        if url not in level1_url:
            last_urls.append(url)
    all_urls=[]
    for url in last_urls:
        all_urls.append(parse.urljoin(domain,url))
        all_urls.append(parse.urljoin(domain,url+"/recommend"))
        all_urls.append(parse.urljoin(domain,url+"/closed"))
    return all_urls

def parse_list():
    res_text=requests.get("https://bbs.csdn.net/forums/J2ME").text
    sel = Selector(text=res_text)
    all_trs = sel.xpath("//table[@class='forums_tab_table']//tr")[2:]
    for tr in all_trs:
        status=tr.xpath("//td[1]/span/text()").extract()[0]
        socre = tr.xpath("//td[1]/em/text()").extract()[0]
        print(status)

    pass
if __name__=="__main__":
    last_urls=get_last_urls()
    parse_list()
    print(last_urls)
    print(len(last_urls))