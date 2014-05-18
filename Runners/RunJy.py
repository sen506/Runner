#coding=utf-8
import os;
import sys;
from AbstractRunner import AbstractRunner;

class RunJy(AbstractRunner):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        
    def run(self):  
        os.system("cls && {0} {1}".format(self.getRunner(), self.getPath()));
        
def main():
    runner = RunCpp("./1.jy");
    runner.run();
    
if(__name__ == "__main__"):
    main();