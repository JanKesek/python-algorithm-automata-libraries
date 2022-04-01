import re

def read_file(fname):
    text=""
    with open(fname,'r') as f:
        text = f.read()
    return text
def read_2_line_input(fname):
    t = []
    with open(fname,'r') as f:
        t = f.readlines()
    return t

def parseFASTA(filename):
    dnas = {}
    key=""
    value=""
    with open(filename,'r') as f:
        for line in f.readlines():
            if line[0]==">":
                if key != "" and value != "":
                    dnas[key]=value.strip()
                    value =""
                key = line.replace(">","").strip()
            else:
                value +=line.strip()
    if key != "" and value != "":
        dnas[key.replace(">","").strip()]=value.strip()
    #print(list(dnas.values()))
    return dnas
def createCodonDic():
    text=""
    codondic={}
    with open('rna_codon_table.txt','r') as f:
        for line in f.readlines():
            codes = re.split("  +", line)
            #print(codes)
            for code in codes:
                codondic[code.split(" ")[0]] = code.split(" ")[1]
    return codondic
def createMonosoicMassTable():
    dic ={}
    with open('monosoic_mass_table.txt','r') as f:
        for line in f.readlines():
            lst = re.split("  +", line)
            dic[lst[0].strip()] = float(lst[1].strip())
    return dic
def saveToFile(s, fname):
    with open(fname, 'w') as f:
        f.write(s)
