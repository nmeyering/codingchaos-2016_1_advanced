#!/usr/bin/env python2
import requests
import sys
import json

r = requests.get("https://api.github.com/repos/{}/{}/pulls".format(sys.argv[1], sys.argv[2]))
res = json.loads(r.text)
res = filter(lambda x: x[u'state'] == 'open', res)
res = ["{}\t{}\t{}".format(x[u'id'], x[u'user'][u'login'], x[u'title']) for x in res]
for x in res:
    print(x)
