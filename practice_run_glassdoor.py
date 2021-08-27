# https://www.glassdoor.com/developer/index.htm

# import json
# import urllib.request

import requests
from bs4 import BeautifulSoup

from get_ip_user_agent import Get_ip_user_agent
from utils import Utils

# #practice2
# r = requests.get('http://whatsmyuseragent.org/')
# soup = BeautifulSoup(r.content, 'lxml')
# section_page = soup.find_all('div', class_="user-agent")
# for ua in section_page:
#     user_agent = ua.p.text
#     print(user_agent)
#


# #practice1
# url = 'http://whatsmyuseragent.org/'
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
# r = requests.get(url, headers = headers)
# print(r)




def build_url(id, key, ip, user_agent):
    base_url = 'http://api.glassdoor.com/api/api.htm'
    query_params =  f"v=1" \
                    f"&format=json" \
                    f"&t.p={id}" \
                    f"&t.k={key}" \
                    f"&action=employers" \
                    f"&q="\
                    f"&userip={ip}" \
                    f"&useragent={user_agent}"

    final_url = f'{base_url}?{query_params}'
    # print(final_url)
    #print(f'Just built this url! \nHier it is the response from glassdoor :\n{final_url}')
    return final_url


#### variables for requests ####
#id, key from json
Utils  = Utils()
config = Utils.get_config()
id = config.get("id")
key = config.get("key")

#ip, useragent from website
page = requests.get('http://whatsmyuseragent.org/')
soup = BeautifulSoup(page.text, 'lxml')
ip, user_agent = Get_ip_user_agent(soup)



#checking the components
# print(f"your id(e-mail address) : {id} \n"
#       f"your key(password) : {key}\n"
#       f"your ip : {ip}\n"
#       f"your user_agent : {user_agent}\n")

#response from api
url = build_url(id, key, ip, user_agent)
print(url)
hdr = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/92.0.4515.159Safari/537.36'}
# hdr = {'User-Agent': 'wtfisthis'}
response = requests.get(url, headers=hdr)

print(response.content)



