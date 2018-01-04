# downloader script
# created by damar
'''
I always using semicolon (;) to prevent myself from forgetting it when code in another language, such as Java
'''
import os, argparse;
try :
    import requests;
except ModuleNotFoundError as e:
    print("I think we missing 'requests' module, please install it first dude");
    # print(e);

class NoLinkException(Exception):
    def __init__(self):
        self.message="no link found in the sources";
        super().__init__(self,self.message)

class LinkEater():
    __slots__=["text_file","files"];

    def __init__(self,text_file:str=None)->None:
        self.text_file=text_file;
        self.files=[];

    def read_from_source(self)->None:
        if self.text_file is None:
            print(" Please feed me some links dude");
        else:
            with open(self.text_file) as file:
                for every_line in file.readlines():
                    self.files.append(every_line[:-1]);
            file.close();
            if len(self.files) == 0:
                raise NoLinkException;
    
    def download(self,link)->bool:
        print(link,end="");
        try:
            res  = requests.get(link);
            with open(link[link.rfind("/")+1:],"wb") as outfile:
                outfile.write(res.content);
            outfile.close();
        except Exception as e:
            print(" ---> Skipped, not tasty, reason :");
            print(e);
            return False;
        print(" ---> EATEN, yummy ");
        return True;

    def process_files(self)->None:
        for every_file in self.files:
            self.download(every_file);
    
    def run(self)->None:
        self.read_from_source();
        self.process_files();
        
def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("text_file",help="text file that contain downloadble links");
    args = parser.parse_args();
    if args.text_file:
        print("downloading from list "+args.text_file);
        eater = LinkEater(args.text_file);
        try:
            eater.run();
        except Exception as e:
            print(e.message);


if __name__ == "__main__":
    main();
