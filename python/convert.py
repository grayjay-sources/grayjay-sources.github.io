import re
from SourceList import *

def parse_gitlab_url(url):
    pattern = r'(?:https?://)?(www\.)?(gitlab\.com)/([^/]+)/'
    match = re.match(pattern, url)
    if match: return match.groups()[1], match.groups()[2]
def parse_github_url(url):
    pattern = r'(?:https?://)?(www\.)?(github\.com)/([^/]+)/'
    match = re.match(pattern, url)
    if match: return match.groups()[1], match.groups()[2]

sourcefile = "sources.json"
# sources = dict_from_file(sourcefile)
sources = source_list_from_file(sourcefile)

# for source in sources:
#     name = source.get("name")
#     if not hasattr(source, "_feeds"): source["_feeds"] = {}

#     commitUrl = source["_feeds"].get("commits")
#     releaseUrl = source["_feeds"].get("releases")
#     print(f'{name}: {commitUrl} {releaseUrl}')
    


# dict_to_file(sourcefile, sources)
source_list_to_file(sourcefile, sources)

input("press key to exit")