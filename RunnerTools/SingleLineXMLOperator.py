#coding=utf-8
import os;
import xml.etree.cElementTree as et;

class SingleLineXMLOperator():
    def __init__(self):
        pass;
        
    @staticmethod
    def writeToFile(dict, fileName):
        root = et.Element("root");
        for key, value in dict.items():
            item = et.SubElement(root, key);
            item.text = value;
        tree = et.ElementTree(root);
        tree.write(fileName, encoding="utf-8", xml_declaration=True);
      
    #structure of dict:
    #{
    #    key:text,
    #    ...
    #}      
    @staticmethod
    def readFromFile(fileName):
        dict = {};
        doc = et.parse(fileName);
        root = doc.getroot();
        for child in root:
            dict.update({child.tag:child.text});
        return dict;
        
    #structure of dict:
    #{
    #    key:(text, attrib, [childNode, ...]),
    #    ...
    #}
    @staticmethod
    def readFromFileEx(fileName):
        dict = {};
        doc = et.parse(fileName);
        root = doc.getroot();
        for child in root:
            dict.update({child.tag:(child.text, child.attrib, [node for node in child])});
        return dict;
            
def main():
    XMLOperator = SingleLineXMLOperator();
    #XMLOperator.writeToFile({"a":"3", "b":"4"}, "./1.txt");
    print(XMLOperator.readFromFileEx(r"C:\Users\sen\Desktop\test\EnvironSetting.xml"));
    
if(__name__ == "__main__"):
    main();