import requests
from optparse import OptionParser
import sys

optparser = OptionParser()
optparser.add_option("--url", dest="url", type="string", default="http://pv36q01ls-geo02064401.geo.apple.com/api/v1/zfs_lookup/search-address-offline-dbt/sdm-address-index-4-27257010.tgz")
# use ssh tunnel to download data in DC
optparser.add_option("--proxy-port", dest="proxy_port", type="string", default="")
(opts, args) = optparser.parse_args()

proxies = None  if opts.proxy_port == "" else {"http": "socks4://127.0.0.1:{}".format(opts.proxy_port)}

print("proxies is {}".format(proxies))

r = requests.get(opts.url, verify=False, proxies=proxies)

if r.status_code != 200:
	print("wrong")
 	sys.exit(-1)
print(r.json().get("url","NO data"))
