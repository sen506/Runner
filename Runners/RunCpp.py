#coding=utf-8
import os;
import sys;
from AbstractRunner import AbstractRunner;

class RunCpp(AbstractRunner):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        
    def run(self):
        os.system("cls && {0}.exe".format(os.path.splitext(self.getBaseName())[0]));
        
def main():
    runner = RunCpp("./1.cpp");
    runner.run();
    
if(__name__ == "__main__"):
    main();