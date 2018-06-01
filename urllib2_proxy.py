# import urllib2
# import socks
# import socket

# proxy = urllib2.ProxyHandler({'http': 'http://localhost:9998'})
# opener = urllib2.build_opener(proxy)
# urllib2.install_opener(opener)
# urllib2.urlopen().read()

import requests 
#import socks

url='http://et02d01ls-maps0001.geo.apple.com:3000/api/v1/services/common-data-dbt'
# url = 'http://pv36q01ls-geo02064401.geo.apple.com/api/v1/zfs_lookup/search-address-offline-dbt/sdm-address-index-4-27257010.tgz'
proxy = {'http': 'socks4://localhost:9998'}

r=requests.get(url, verify=False, proxies=proxy)
print r.json()
