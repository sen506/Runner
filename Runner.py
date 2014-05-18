#coding=utf-8
import os;
import sys;
sys.path.append(r".\RunnerException");
sys.path.append(r".\Runners");
sys.path.append(r".\RunnerTools");
from RunnerExceptions import *;
from RunnerFactory import RunnerFactory;
        
            
def main():
    """
    print(sys.path);
    factory = RunnerFactory("./RunnerConfig/EnvironSetting.xml", "./RunnerConfig/LangSetting.xml");
    #print(os.environ["classpath"]);
    #os.system("pause");
    runner = factory.createRunner(r".\test\test.c");
    runner.start();
    """
#    """
    if(len(sys.argv) > 1):
        factory = RunnerFactory("./RunnerConfig/EnvironSetting.xml", "./RunnerConfig/LangSetting.xml");
        try:
            runner = factory.createRunner(sys.argv[1]);
            runner.start();
        except Exception as e:
            print(e);
        finally:
            os.system("pause");
#    """
    
if(__name__ == "__main__"):
    main();