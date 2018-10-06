#!/usr/bin/python
# coding: utf-8

import sys
import subprocess
from os.path import exists

def padding( t ) :
	ret = ""
	for i in t.split(":"):
		ret += i.rjust(2, "0") + ":"
	ret = ret[:-1]
	while len(ret.split(":")) < 3:
		ret = "00:" + ret
	return ret

def time_to_second( t ):
	l = t.split(":")
	if len(l) > 3:
		print("Error in time format")
		raise SystemExit(-2)
	m = len(l)
	k = 1
	ret = 0
	for i in range(m):
		ret += int(l[m-i-1]) * k
		k *= 60
	return ret

def diff_time(t1, t2):
	tt1 = time_to_second(t1)
	tt2 = time_to_second(t2)
	d = tt2 - tt1
	if d < 0:
		print("End time must be greater than start time.")
		raise SystemExit(-1)
	ret = str(d // 3600)
	d %= 3600
	ret += ":" + str( d // 60 )
	d %= 60
	ret += ":" + str( d )
	return padding(ret)

def file_with_counter( f, cpt, ext):
	return f + "_" + str( cpt ).rjust(4, "0") + ext
	
def output_filename( f ):
	while f[-1] == ".":
		f = f[:-1]
	ext = "." + f.split(".").pop()
	if "." in f:
		f = f[:-len(ext)]
	else:
		ext = ""
	cpt = 1
	while exists( file_with_counter( f, cpt, ext ) ) :
		cpt += 1
		if cpt >= 9999:
			print("All output filenames already exist.")
			raise SystemExit(-3)
			
	return file_with_counter( f, cpt, ext )
	
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "Usage : %s start_time end_time input_file" % sys.argv[0]
		print "time : hh:mm:ss"
		exit(0)
	
	cmd = ["ffmpeg"]
	cmd.append("-i")
	cmd.append(sys.argv[3])
	cmd.append("-ss")
	cmd.append(padding(sys.argv[1]))
	cmd.append("-t")
	cmd.append(diff_time(sys.argv[1], sys.argv[2]))
	cmd.append("-async")
	cmd.append("1")
	cmd.append("-c")
	cmd.append("copy")
	cmd.append(output_filename(sys.argv[3]))
	p = subprocess.Popen(cmd).wait()
