
import requests as rq
from bs4 import BeautifulSoup as bsa
import re
URL = "https://tutortop.ru/courses_category/programmirovanie/"
COURSE = "https://tutortop.ru/courses_selection/"


data = rq.get(URL).text

soup = bsa(data, 'lxml')

list_courses = soup.find_all('div', class_='tab-course-item tab-course-item-bg')



reg = r'[0-9]+ [0-9]+'


# what = re.findall(reg, str(list_courses))

# #.?+.[a-z]+.=+.[0-9]+

# print(what)
# print(list_courses[0])
# #print(re.findall(reg,list_courses))


result_dict = {}
for x in list_courses[:1]:
    
    result_dict['text'] = str(x.text).strip()
    result_dict['link'] = str(x.a).replace('<a class="tab-link-course" href="','').replace('" rel="nofollow" target="_blank">Ссылка на курс</a>', '')
    

print(result_dict['text'])
print(re.findall(reg, result_dict['text'])[-2:])