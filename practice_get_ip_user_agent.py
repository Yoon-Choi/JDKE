from bs4 import BeautifulSoup
import requests

def prctice_Get_ip_user_agent(soup):
    paragraphs = soup.find_all(text=True)
    #print(type(paragraphs))
    ip = ''
    user_agent = ''
    for p in paragraphs:
        if 'python' in p:
            user_agent = p

        if 'My IP Address' in p:
            parse_result = str(p).split(": ")
            ip = parse_result[1]
    return ip,user_agent



#def Get_ip_user_agent(soup):
    # paragraph = soup.find_all('p', class_='intro-text')
    # for par in paragraph:
    #     user_agent = par
    # return print(user_agent)




# ip, useragent from website
#page = 'http://whatsmyuseragent.org/'
#soup = BeautifulSoup(page.text, 'lxml')

# ip = '1234'
# user_agent = ''
#
# url = 'http://whatsmyuseragent.org/'
# class_ = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
# response = requests.get(url, class_=class_)
# print(response.content)

#user_agent = Get_ip_user_agent(soup)


    # asdf = soup.find_all('div', class_='user-agent')
    # for a in asdf:
    #     user_agent = a.p
    #
    # return ip, user_agent



    # user_agent = soup.find('p', class_='intro-text').text

    # print(user_agent)



    # paragraphs = soup.find_all(text=True)
    # #print(type(paragraphs))
    # ip = '1234'
    # user_agent = ''
    # for p in paragraphs:
    #
    #     # if 'python' in p:
    #     #     user_agent = p
    #
    #     if 'My IP Address' in p:
    #         parse_result = str(p).split(": ")
    #         ip = parse_result[1]
    # return ip, user_agent


# #checking the components
# print(f"your id(e-mail address) : {id} \n"
#       f"your key(password) : {key}\n"
#       f"your ip : {ip}\n"
#       f"your user_agent : {user_agent}\n")