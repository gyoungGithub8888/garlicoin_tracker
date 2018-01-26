import urllib.parse
import urllib.request

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib.request.Request("https://explorer.grlc-bakery.fun/tx/1819f644b068a7fc125b15683f150c45a3c601dfaa0d23d4a06d8964f5b77270", None, headers)
web = urllib.request.urlopen(req)
webbytes = web.read()
webstr = webbytes.decode("utf-8")
web.close()
print(webstr)
test = webstr.find('Recipients',1)
webstr_truncated = webstr[test:]