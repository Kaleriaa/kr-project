import re

def find_domains(str):
    founded = re.search("@[\w.]+", str)
    if (founded == None):
        return 'Incorrect string'
    return founded.group()