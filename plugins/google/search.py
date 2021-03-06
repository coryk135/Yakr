from yakr.plugin_base import *
import urllib2
import json
_API_URL = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" 

@command("gs")
def search(who, what, where):
    reply_json = urllib2.urlopen(_API_URL + urllib2.quote(what)).read()
    response = json.loads(reply_json)
    data = response['responseData']
    if "results" not in data or len(data['results']) == 0:
        say(where, "No results :(")
        return

    result = data['results'][0]
    reply = "<{C3}Google Search{}: {B}%s{} | {LINK}%s{} >" % (
            result['titleNoFormatting'], 
            urllib2.unquote(result['url']))
    say(where, reply)
