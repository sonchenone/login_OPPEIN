# -*- coding: UTF-8 -*-
# ！/usr/bin/env python3
# Author:  Murphy
#  Blog :  www.moyo1.cn

import os
import re
import requests
from time import sleep
from bs4 import BeautifulSoup


class CollectNovel(object):
    def __init__(self):
        self.novel_data = {}
        self.start_url = "https://www.ddxsku.com/full.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}

    def collect_url(self):
        print("Collecting novel basic data.....")
        start_response = requests.get(self.start_url, headers=self.headers)
        total_page = re.search(r'<em id="pagestats">1/(.+)</em>', start_response.text).group(1)
        novel_navigation_urls = [fr"http://www.ddxsku.com/modules/article/articlelist.php?fullflag=1&page={i}" for i in
                                 range(1, int(total_page) + 1)]

        for novel_navigation_url in novel_navigation_urls:
            novel_navigation_response = requests.get(novel_navigation_url, headers=self.headers)
            novel_index_urls = re.findall('<td class="L"><a href="(.+)" title=".+" target="_blank">.+</a></td>',
                                          novel_navigation_response.text)

            for novel_index_url in novel_index_urls:
                novel_index_response = requests.get(novel_index_url, headers=self.headers)
                novel_index_response.encoding = "utf-8"

                novel_name = re.search(fr'.+<a >(.+)</a>.+', novel_index_response.text).group(1)
                novel_author = re.search(r'<dd><h3>作者：(.+)</h3><br>.+</h3></dd>', novel_index_response.text).group(1)
                self.novel_data = {novel_name: [("novel_author", novel_author)]}
                print("Collecting novel:  《%s》--%s" % (novel_name, novel_author))

                index_soup = BeautifulSoup(novel_index_response.text, "html.parser")
                novel_text_urls = index_soup.find_all("td", class_="L")
                for each in novel_text_urls:
                    chapters_title = each.text
                    chapters_url = each.a["href"]
                    self.novel_data[novel_name].append((chapters_title, chapters_url))
                sleep(1)
                # break  # 调试减少运行时间使用，爬取全站删除此处即可。
            break  # 调试减少运行时间使用，爬取全站删除此处即可。

    def novel_copy(self):
        self.collect_url()
        if self.novel_data:
            for name in self.novel_data:
                count = 0
                print("Downloading:  《%s》" % name, end="\n" * 2)

                work_path = r"C:/Users/Administrator/Desktop/NovelCopy/%s-%s" % (name, self.novel_data[name][0][1])
                if not os.path.exists(work_path):
                    os.makedirs(work_path)
                    os.chdir(work_path)
                else:
                    os.chdir(work_path)

                for chapter_data in self.novel_data[name][1:]:
                    count += 1
                    print("Downloading:  《%s》--%s" % (name, chapter_data[0]))
                    chapter_response = requests.get(chapter_data[1], headers=self.headers)
                    chapter_response.encoding = "utf-8"

                    chapter_soup = BeautifulSoup(chapter_response.text, "html.parser")
                    chapter_text = chapter_soup.find("dd", id="contents")
                    with open("%d-%s.txt" % (count, chapter_data[0]), "w", encoding="utf-8") as f:
                        f.write(chapter_text.text)
                    sleep(2)
                print()
                break
        else:
            print("Collect data failed")


if __name__ == "__main__":
    novel = CollectNovel()
    novel.novel_copy()