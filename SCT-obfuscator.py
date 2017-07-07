# Author: Mr.Un1k0d3r - RingZer0 Team 2017
# COM Scriptlet payload obfuscator

import sys
import random
import string 

def gen_str(size):
	return "".join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(size)) 

if __name__ == "__main__":
	print "COM Scriptlet payload (SCT file) obfuscator"
	print "Mr.Un1k0d3r - RingZer0 Team 2017\n\n"
	if len(sys.argv) < 2:
		print "Usage %s [sct file path]" % sys.argv[0]
		exit(0)
		
	original = ""
	try:
		for line in open(sys.argv[1], "rb").readlines():
			if not line[:1] == "'":
				original += line
	except:
		print "[-] Failed to open %s" % sys.argv[1]
		exit(0)
		
	for i in range(0, 256):
		newval = random.randint(1, 100)
		original = original.replace("(%d)" % i, "(%d-%d)" % (i + newval, newval))
		
	for var in ["objExcel", "WshShell", "RegPath", "action", "objWorkbook", "xlmodule","Win32COMDebug"]:
		newvar = gen_str(random.randrange(5, 25))
		original = original.replace(var, newvar)
		
	open("%s.edit" % sys.argv[1], "wb").write(original)
	print "[+] new payload was saved to %s" % sys.argv[1] + ".edit"
