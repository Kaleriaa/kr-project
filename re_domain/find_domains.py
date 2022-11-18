import re

def find_domains(str):
    return re.search("@[\w.]+", str).group()