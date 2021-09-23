# https://www.glassdoor.com/developer/index.htm
#순서가 중요한 것 같아 보인다
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

    print(f'Just built this url! \nHer it is the response from glassdoor :\n{final_url}')
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
print(f"your id(e-mail address) : {id} \n"
      f"your key(password) : {key}\n"
      f"your ip : {ip}\n"
      f"your user_agent : {user_agent}\n")

#response from api
url = build_url(id, key, ip, user_agent)
