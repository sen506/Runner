#coding=utf-8
import os;
import sys;
from AbstractRunner import AbstractRunner;

class RunHtm(AbstractRunner):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        
    def run(self):
        os.system("cls && {0} {1}".format(self.getRunner(), self.getPath()));
        
def main():
    runner = RunHtml(r"C:\Users\sen\Desktop\form.htm");
    runner.run();
    
if(__name__ == "__main__"):
    main();