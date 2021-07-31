# https://www.glassdoor.com/developer/index.htm

from requests import get
from utils import Utils
from bs4 import BeautifulSoup


def get_ip_user_agent(soup_page):
    paragraphs = soup.find_all(text=True)
    print(type(paragraphs))
    ip = ''
    user_agent = ''
    for p in paragraphs:
        if "python" in p:
            user_agent = p
        if 'My IP Address' in p:
            parse_result = str(p).split(": ")
            ip = parse_result[1]

    return ip, user_agent


def build_url():
    base_url = 'http://api.glassdoor.com/api/api.htm'
    query_params = f"t.p={config['id']}" \
                   f"&t.k={config['key']}" \
                   f"&userip={ip}" \
                   f"&useragent={user_agent}" \
                   f"&format=json" \
                   f"&v=1" \
                   f"&action=employers" \
                   f"&q="
    final_url = f'{base_url}?{query_params}'

    print(f'Just built this url! \nHer it is:\n{final_url}')
    return final_url


# variables for requests
config = Utils.config
page = get('http://whatsmyuseragent.org/')
soup = BeautifulSoup(page.text, 'lxml')
ip, user_agent = get_ip_user_agent(soup)

url = build_url()
