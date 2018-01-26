import urllib.parse as urlParse
import urllib.request as urlRequest
import csv

#----------------------Constants---------------------------------
# markers chosen to find ADDRESS [0,1] and AMOUNT [2,3]
markers = [
	'<a href="/address/',
	'" class="loading">',
	'<td class="success">',
	' GRLC'
]

strCut 			= 'Recipients'
hashtxFileName 	= 'testHashtx.txt'
explorertxURL 	= 'https://explorer.grlc-bakery.fun/tx/'

# spoof browser to get past bot-blocking
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
#-------------------------Functions------------------------------
def read_page(hashID, URLinfo)
	req = urlRequest.Request(URLinfo.url+hashID, None, URLinfo.headers)
	web = urlRequest.urlopen(req)
	webbytes = web.read()
	webstr = webbytes/decode("utf-8")
	web.close()
	return webstr

def truncate_page(webstr,strCut)
	indexCut = webstr.find(strCut)
	webstrCut = webstr[indexCut:]
	return webstrCut

def find_str(webstr,markerStart,markerEnd)
	indexStart 	= webstr.find(markerStart) + len(markerStart)
	indexEnd 	= webstr.find(markerEnd)
 	strOut 		= webstr[indexStart:indexEnd]
 	return strOut
 	
class URLinfo
	def __init__(self, URL, headers)
		self.url = URL
		self.headers = headers

#----------------------Setup-------------------------------------
headers = { 'User-Agent' : user_agent } #set browser header

#make list with tx hash for each item
hashtxList = []
with open(hastxFileName, newline = ',') as inputfile:
	for row in csv.reader(inputfile):
		hashtxList.append(row)
info = URLinfo(explorertxURL,headers)
# ---------------------Begin Loop--------------------------------
# --------Initializing
hashID 	= []
URL 	= []


for i in hashtxList
	hashID 	= hashtxList[i]

	webstr = read_pag(hashID, info)
	webstrCut = truncate_page(webstr,strCut)

	isValidIndex = 1
	while isValidIndex > -1
		addressTemp = find_str(webstrCut,markers[0],markers[1])
		amountTemp  = find_str(webstrCut,markers[2],markers[3])

		isValidIndex = webstrCut.find(markers[0])
#----------------------End Loop----------------------------------