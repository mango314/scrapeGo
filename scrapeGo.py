import scraperwiki, urllib2
from bs4 import BeautifulSoup

def scrape():
	u=file("cho-1-elementary.pdf")

	x=scraperwiki.pdftoxml(u.read())
	soup = BeautifulSoup(x)
	book = soup.get_text().split('\n')

	page = []
	newpage = []
	for x in  book[36:]:
		newpage += [x]
		if x == '':
			pass
		elif x[0] == 'p':
			page += [newpage]

			newpage = []
		elif x[0] == '<':
			newpage = [x]
	return page

'''(;AB[qm][qo][ro][rp][kq][lq][qq][mr][nr][or][qr][qs]
AW[po][lp][pp][qp][mq][nq][oq][rq][pr][rr][rs])
'''
problems = scrape()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
keys = { i: alphabet[i] for i in range(26)}
print keys

for row in problems[0]:
	print row

out = file("Cho1.sgf", "w")

#print '''(C[Cho Chikun's Encyclopedia of Life & Death (Vol 1)]'''
out.write("(;C[Cho Chikun's Encyclopedia of Life & Death (Vol 1)]\n")
for k, p in enumerate(problems[:]):
	black = 'AB'
	white = 'AW'
	for i, row in enumerate(p):
		black += ''.join([ '[%s%s]'%(keys[i],keys[j]) for j, c in enumerate(row) if c == '@'])
		white += ''.join([ '[%s%s]'%(keys[i],keys[j]) for j, c in enumerate(row) if c == '!'])
	#print '(;%s%sC[problem %s])' %(black, white, k+1)
	out.write( '(;%s%sC[problem %s])\n' %(black, white, k+1))
#print ')'
out.write(')')
