#coding=utf-8
import sys;
sys.path.append(r"..\RunnerException");
sys.path.append(r"..\RunnerConfig");
sys.path.append(r"..\RunnerTools");
from __init__ import *;
from RunnerExceptions import *;
from SingleLineXMLOperator import SingleLineXMLOperator;
from ReplaceVariable import ReplaceVariable;
import os;
import time;

class RunnerFactory():
    def __init__(self, envFile, langFile):
        self.setEnvFilePath(envFile);
        self.setLangFilePath(langFile);
        
    def setEnvFilePath(self, envFile):
        self._envFilePath = envFile;
        self._loadEnv(envFile);
        
    def getEnvFilePath(self):
        return self._envFilePath;
        
    def setLangFilePath(self, langFile):
        self._langFilePath = langFile;
        
    def getLangFilePath(self):
        return self._langFilePath;
        
    def _loadEnv(self, fileName):
        path, name = os.path.split(fileName);
        processedFile = r"{0}\p_{1}".format(path, name);
        if(os.path.exists(processedFile) and os.path.getmtime(processedFile) > os.path.getmtime(fileName)):
            dict = SingleLineXMLOperator.readFromFile(processedFile);
        else:
            dict = ReplaceVariable.replace(SingleLineXMLOperator.readFromFile(fileName))
            SingleLineXMLOperator.writeToFile(dict, processedFile);
        for key, value in dict.items():
            try:
                env = os.environ[key];
            except:
                env = "";
            os.environ.putenv(key, "{0};{1}".format(value, env));
        
    def _initRunner(self, runner, extName):
        langSetting = SingleLineXMLOperator.readFromFile(self.getLangFilePath())[extName].split(";");
        if(len(langSetting) != 4):
            raise IncorrectFormatException("LangSetting.xml设置错误!");
        runner.setPrecompiledEnv(langSetting[0].strip() == "" and "echo > nul" or langSetting[0]);
        runner.setCompiler(langSetting[1]);
        runner.setRunner(langSetting[2]);
        runner.setParameter(langSetting[3]);
        
        
    def createRunner(self, fileName):
        extName = fileName.split(".")[-1].lower();
        """
        moduleName = "Run" + extName.capitalize();
        if(not os.path.exists(moduleName + ".py")):
            raise ModuleNotFoundException(moduleName + "模块不存在!");
        module = __import__(moduleName);
        runnerClass = getattr(module, moduleName);
        runner = runnerClass(fileName);
        """
        if(extName == "cpp" or extName == "c"):
            runner = RunCpp(fileName);
            
        elif(extName == "java"):
            runner = RunJava(fileName);
            
        elif(extName == "py"):
            runner = RunPy(fileName);
            
        elif(extName == "html" or extName == "html"):
            runner = RunHtml(fileName);
        
        elif(extName == "xml"):
            runner = RunXml(fileName);
            
        elif(extName == "bat" or extName == "cmd"):
            runner = RunBat(fileName);
        
        elif(extName == "vbs" or extName == "vba"):
            runner = RunVbs(fileName);
            
        elif(extName == "jy"):
            runner = RunJy(fileName);
            
        else:
            raise UnrecognizedExtNameException("识别不了的扩展名!");
        
        self._initRunner(runner, extName);
        return runner;
        
def main():
    factory = RunnerFactory("../RunnerConfig/EnvironSetting.xml", "../RunnerConfig/LangSetting.xml");
    runner = factory.createRunner(r"..\test\test.cpp");
    runner.start();
    
if(__name__ == "__main__"):
    main();