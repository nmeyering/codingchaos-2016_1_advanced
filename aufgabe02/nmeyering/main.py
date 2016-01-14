import requests
import sys
import json

repo = sys.argv[1]
r = requests.get("https://api.github.com/repos/{}/{}/pulls".format(repo, repo))
res = json.loads(r.text)
res = filter(lambda x: x[u'state'] == 'open', res)
res = ["{}\t{}\t{}".format(x[u'id'], x[u'user'][u'login'], x[u'title']) for x in res]
for x in res:
    print(x)
