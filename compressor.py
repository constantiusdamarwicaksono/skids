#!/usr/bin/python3
from glob import glob
from PIL import Image
from os import listdir
from io import BytesIO
from shutil import copyfile
import sys,os

class digger():
	def __init__(self,path,quality,limit):
		self.path=path;
		self.count=0;
		self.quality=quality;
		self.limit=int(limit);
		self.comp_path='compressed_'+path;
	def run(self):
		if not os.path.isdir(self.comp_path):
			os.mkdir(self.comp_path);
		self.dig(self.path);
	def dig(self,path):
		for dir in listdir(path):
			if os.path.isdir(path+dir):
				print(dir+' is child of '+path);
				if not os.path.isdir('compressed_'+path+dir):
					os.mkdir('compressed_'+path+dir);
				self.dig(path+dir+'/');
			elif dir.lower().endswith(('png','jpeg','gif','jpg')) :
				try:
					start = os.stat(path+dir).st_size;
					if(start/1024>self.limit):
						img=Image.open(path+dir);
						dummy_file = BytesIO();
						img.save(dummy_file,format=img.format,quality=int(self.quality),optimize=True,compression_level=9);
						if int(dummy_file.tell()/1024) < int(start/1024):
							img.save('compressed_'+path+dir,format=img.format,quality=int(self.quality),optimize=True,compression_level=9);
						else:
							copyfile(path+dir,'compressed_'+path+dir);	
						dummy_file.close();
						end = os.stat('compressed_'+path+dir).st_size;
						loss_percentage = round(((end/start)*100),1);
						print('compressing file : '+dir+' -> '+str(loss_percentage)+'%');
						self.count+=1;
						img.close();
					else:
						copyfile(path+dir,'compressed_'+path+dir);
				except Exception as e:
					print(e);


def main():
    root=sys.argv[1];
    quality=sys.argv[2];
    limit=sys.argv[3];
    dig = digger(root,quality,limit);
    dig.run();
    print('total images : '+str(dig.count));


if __name__ =='__main__':
    main();
