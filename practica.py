import re

while(1):
	pag=raw_input("\n\nEscribe la direccion\n:>>  ") 

	if re.match("((https|http|ftp)://)(www.)([a-z0-9].?)+(.([a-z0-9][a-z0-9][a-z0-9]))+((/\w-)*)",pag):
		a = pag.split("://")
		b = a[1].split("/")
		#url=list(a)
		print "\nprotocol: "+a[0]
		print "domain: "+b[0]
		if len(b)==2:
			print "path: "+b[1]
		else:
			print "empty string"
	elif re.match("(www.)([a-z0-9].?)+(.([a-z0-9][a-z0-9][a-z0-9]))+((/\w-)*)",pag):
		print "\nempty protocol"
		b = pag.split("/",1)
		print "domain: "+b[0]
		if len(b)>=2:
			print "path: "+str(b[1])
		else:
			print "empty string"

	else:
		print "Direccion incorrecta"
	#http://www.mysite.com/path-student-files