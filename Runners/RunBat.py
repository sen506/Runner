#coding=utf-8
import os;
import sys;
from AbstractRunner import AbstractRunner;

class RunBat(AbstractRunner):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        
def main():
    runner = RunCpp("./1.cpp");
    runner.run();
    
if(__name__ == "__main__"):
    main();