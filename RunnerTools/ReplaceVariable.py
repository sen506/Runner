import gc;
import re;
import os;
from SingleLineXMLOperator import SingleLineXMLOperator as reader;

regFindVariable = re.compile("(%.*?%)");
regFindWildCard = re.compile(r";?([^\s]+\\\*);?");

class ReplaceVariable():
    def __init__(self):
        pass;
        
    @staticmethod
    def _replaceVar(dict, key, visit):
        if(regFindVariable.search(dict[key]) != None):
            visit[key.lower()] = True;
            vars = regFindVariable.findall(dict[key]);
            for var in vars:
                #print("var:" + var + "  var.strip.lower:" + var.strip("%").lower());
                if(not visit[var.strip("%").lower()]):
                    dict[key] = dict[key].replace(var, ReplaceVariable._replaceVar(dict, var.strip("%").lower(), visit));
            visit[key.lower()] = False;
        return dict[key];
        
    @staticmethod
    def _replaceWildcard(dict, key):
        pathList = dict[key].split(";");
        for rawPath in pathList:
            if(regFindWildCard.search(rawPath) != None): 
                list = [];
                path = rawPath.strip("*");
                for filename in os.listdir(path):
                    file = path + filename;
                    if(os.path.isfile(file)):
                        list.append(file);
                dict[key] = dict[key].replace(rawPath, ";".join(list));
        
    @staticmethod
    def replace(dict):
        gc.disable();
        visit = {};
        for key in dict.keys():
            visit.update({key.lower():False});
        for key in dict.keys():
            ReplaceVariable._replaceVar(dict, key, visit);
            ReplaceVariable._replaceWildcard(dict, key);
        #print(dict);
        gc.enable();
        return dict;
            
def main():
    #print(regFindWildCard.findall(r"D:\Java Jars\spring-framework-4.04\libs\*"));
    ReplaceVariable.replace({"path":r"E:\ApkTool\*"});
    """
    D:\Java Jars\spring-framework-4.04\libs\*
    dict = reader.readFromFile("./EnvironSetting.xml");
    #print(dict);
    #print("");
    ReplaceVariable.replace(dict);
    print(dict);
    """
    
if(__name__ == "__main__"):
    main();