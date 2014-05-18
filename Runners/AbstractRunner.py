#coding=utf-8
import os;
import sys;
import time;

class AbstractRunner():
    def __init__(self, path):
        self._param = "";
        self._pe = "echo > nul";
        self._cp = "";
        self._runner = "";
        self.setPath(path);
        
    def setPath(self, path):
        self._path = path;
        self._setNames(path);
     
    def getPath(self):
        return self._path;
        
    def _setNames(self, path):
        self._dirName = os.path.dirname(path);
        self._baseName = os.path.basename(path);
        
    def getDirName(self):
        return self._dirName;
        
    def getBaseName(self):
        return self._baseName;
        
    def setParameter(self, param):
        self._param = param;
        
    def getParameter(self):
        return self._param;
        
    def setPrecompiledEnv(self, pe):
        self._pe = pe;
        
    def getPrecompiledEnv(self):
        return self._pe;
        
    def setCompiler(self, cp):
        self._cp = cp;
        
    def getCompiler(self):
        return self._cp;
        
    def setRunner(self, runner):
        self._runner = runner;
        
    def getRunner(self):
        return self._runner;
        
    def start(self):
        if(self.compile() == 0):
            start = time.time();
            self.run();
            print("\n\nTime:{0:.4f}s".format(time.time() - start));
        
    def compile(self):
        os.chdir(self.getDirName());
        ret = 0;
        if(self.getCompiler() != ""):
            ret = os.system("{0} && {1} {2} {3}".format(self.getPrecompiledEnv(), self.getCompiler(), self.getBaseName(), self.getParameter()));
        return ret;
        
    def run(self):
        os.system("cls && {0} {1}".format(self.getRunner(), self.getPath()));
        
def main():
    runner = AbstractRunner(r"C:\Users\sen\Desktop\test\test.jy");
    runner.run();

if(__name__ == "__main__"):
    main();