#coding=utf-8
class UnrecognizedExtNameException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg);
        
class ModuleNotFoundException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg);
        
class IncorrectFormatException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg);
        
def main():
    try:
        raise ModuleNotFoundException("模块不存在!");
    except ModuleNotFoundException as e:
        print(e);
        
if(__name__ == "__main__"):
    main();