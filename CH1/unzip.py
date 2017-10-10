import zipfile
import optparse
from threading import Thread
def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print "[+] Found Password: " + password + "\n"
	except:
		pass
def main():
	# use optparse to provide zip and dic files flag options
	parser = optparse.OptionParser("usage%prog " +\
	"-f <zipfile> -d <dictionary>")
	parser.add_option("-f", dest="zname", type="string",\
	help="specify zip file")
	parser.add_option("-d", dest="dname", type="string",\
	help="specify dictionary file")
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname== None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname
	zFile = zipfile.ZipFile("secret.zip")
	passFile = open("dictionary.txt")
	for line in passFile.readlines():
		password = line.strip("\n")
		# use multi-thread to increase performance
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()
if __name__ == "__main__":
	main()
