#coding=utf-8
from AbstractRunner import AbstractRunner;
import os;

class RunPy(AbstractRunner):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        
        
def main():
    runner = RunPython("./1.py");
    runner.run();
    
if(__name__ == "__main__"):
    main();