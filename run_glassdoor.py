# https://www.glassdoor.com/developer/index.htm

# import json
import requests
from bs4 import BeautifulSoup

from get_ip_user_agent import Get_ip_user_agent
from utils import Utils



def build_url(id, key, ip, user_agent):
    base_url = 'http://api.glassdoor.com/api/api.htm'
    query_params = f"t.p={id}" \
                   f"&t.k={key}" \
                   f"&userip={ip}" \
                   f"&useragent={user_agent}" \
                   f"&format=json" \
                   f"&v=1" \
                   f"&action=employers" \
                   f"&q="
    final_url = f'{base_url}?{query_params}'

    print(f'Just built this url! \nHer it is:\n{final_url}')
    return final_url


#### variables for requests ####
#id, key from json
Utils  = Utils()
config = Utils.config
id = config.get("id")
key = config.get("key")
#ip, useragent from website
page = get('http://whatsmyuseragent.org/')
soup = BeautifulSoup(page.text, 'lxml')
ip, user_agent = Get_ip_user_agent(soup)
#final_url
url = build_url(id, key, ip, user_agent)
