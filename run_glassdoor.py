#import urllib2, sys
#from BeautifulSoup import BeautifulSoup
#
param_constants = {'id': '',
                   'key': '',
                   'ip_address': '',
                   'user_agent': '',  # web browser?
                   'format' : '',
                    'v' : ''
}


def build_url():
    base_url = 'http://api.glassdoor.com/api/api.htm'
    query_params = f"t.p={param_constants['id']}" \
                   f"&t.k={param_constants['key']}" \
                   f"&userip={param_constants['ip_address']}" \
                   f"&useragent={param_constants['user_agent']}" \
                   f"&format=json" \
                   f"&v=1" \
                   f"&action=employers" \
                   f"&q="
    final_url = f'{base_url}?{query_params}'

    print(f'Just built this url! \nHer it is:\n{final_url}')
    return final_url


url = build_url()


#hdr = {'User-Agent': 'Mozilla/5.0'}
#req = urllib2.Request(url,headers=hdr)
#response = urllib2.urlopen(req)
#soup = BeautifulSoup(response)