#!/usr/bin/python3
from glob import glob
from PIL import Image
from os import listdir
import sys,os

class digger():
	def __init__(self,path,limit):
		self.path=path;
		self.count=0;
		self.limit=limit;
		self.comp_path='compressed_'+path;
	def run(self):
		if not os.path.isdir(self.comp_path):
			os.mkdir(self.comp_path);
		self.dig(self.path);
	def dig(self,path):
		for dir in listdir(path):
			if os.path.isdir(path+dir):
				print(dir+' is child of '+path);
				#if not os.path.isdir('compressed_'+path+dir):
				#	os.mkdir('compressed_'+path+dir);
				self.dig(path+dir+'/');
			elif dir.lower().endswith(('png','jpeg','gif','jpg')) :
				try:
					start = os.stat(path+dir).st_size;
					if start/1024 >= int(self.limit) :
						self.count+=1;
						print(dir+' filesize : '+ str(start/1024)+' KB');
					#img=Image.open(path+dir);
					#img.save('compressed_'+path+dir,quality=int(self.quality),optimize=True);
					#end = os.stat('compressed_'+path+dir).st_size;
					#print('compressing file : '+dir+' -> '+str(round(((end/start)*100),1))+'%');
					#self.count+=1;
					#img.close();
				except Exception as e:
					print(e);


def main():
    root=sys.argv[1];
    size_limit=sys.argv[2];
    dig = digger(root,size_limit);
    dig.run();
    print('total images : '+str(dig.count));


if __name__ =='__main__':
    main();
