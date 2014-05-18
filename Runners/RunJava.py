#coding=utf-8
import os;
import re;
from AbstractRunner import AbstractRunner;

regRunnable = re.compile(r"(\s*public\s+static\s+void\s+main\(\s*String\s+.+\))");
regFindPackage = re.compile(r"\s*package\s+([^;]*)");

class Runnable():
    def __init__(self, path):
        pass;
        
    def setPath(self, path):
        self._path = path;
        
    def getPath(self):
        return self._path;
        
    def runnable(self):
        file = open(self.getPath(), "r");
        ret = (None != regRunnable.search(file.read()));
        file.close();
        return ret;

class _RunJavaWithPackage(AbstractRunner, Runnable):
    def __init__(self, path, packageName):
        AbstractRunner.__init__(self, path);
        Runnable.__init__(self, path);
        self.setPackageName(packageName);
       
    def setPackageName(self, packageName):
        self._packageName = packageName;
        
    def getPackageName(self):
        return self._packageName;
        
    def compile(self):
        return os.system("{0} -d . {1}".format(self.getCompiler(), self.getBaseName()));
        
    def run(self):
        os.system("cls && {0} {1}.{2}".format(self.getRunner(), self.getPackageName(), os.path.splitext(self.getBaseName())[0]));

class _RunJava(AbstractRunner, Runnable):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        Runnable.__init__(self, path);

    def runnable(self):
        file = open(self.getPath(), "r");
        ret = (None != regRunnable.search(file.read()));
        file.close();
        return ret;
        
    def run(self):
        os.system("cls && {0} {1}".format(self.getRunner(), os.path.splitext(self.getBaseName())[0]));
        
class RunJava(AbstractRunner):
    def __init__(self, path):
        AbstractRunner.__init__(self, path);
        packageName = self.getPackageName();
        if(packageName != ""):
            self._runner = _RunJavaWithPackage(path, packageName);
        else:
            self._runner = _RunJava(path);
        
    def getPackageName(self):
        file = open(self.getPath(), "r");
        try:
            package = regFindPackage.findall(file.read())[0].strip();
        except:
            package = "";
        file.close();
        return package;
    
    def setCompiler(self, cp):
        self._runner.setCompiler(cp);
        
    def setRunner(self, runner):
        self._runner.setRunner(runner);
        
    def setPrecompiledEnv(self, pe):
        self._runner.setPrecompiledEnv(pe);
    
    def setParameter(self, param):
        self._runner.setParameter(param);
    
    def runnable(self):
        file = open(self.getPath(), "r");
        ret = (None != regRunnable.search(file.read()));
        file.close();
        return ret;
        
    def compile(self):
        os.chdir(self.getDirName());
        return self._runner.compile();
        
    def run(self):
        if(self._runner.runnable()):
            self._runner.run();
        
        
        
        
def main():
    runner = RunJava("./SimpleHello.java");
    print(regFindPackage.findall("  package      test"));
    print(runner.getMain());
    #runner = RunJava("./SimpleHello.java");
    #runner.run();
    
if(__name__ == "__main__"):
    main();