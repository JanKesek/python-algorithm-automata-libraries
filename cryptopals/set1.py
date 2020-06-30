import base64
import codecs
import string
import binascii
import collections
import re
from english_frequency import get_frequency_alphabet
def hex_to_base64(s):
    #return base64.b64encode(s)
    return codecs.encode(codecs.decode(s,'hex'),'base64').decode().strip()
def fixed_xor(a,b):
    xorint= int(a,16) ^ int(b,16)
    return hex(xorint)
def single_byte_xor_cipher(s):
    most_common=get_frequency_alphabet()
    scoredic={}
    ord_encoded=[int(c) for c in binascii.unhexlify(s)]
    for char in string.ascii_lowercase:
        xored=[chr(c^ord(char)) for c in ord_encoded]
        c=''.join(xored)
        c= c.replace('\r', '').replace('\n', '')
        c=c.replace('\x07','').replace('\x00',' ')
        scoredic[c]=score_str_similiarity(c,most_common)
    #max_k=max(scoredic,key=scoredic.get)
    max_v=0
    max_k=''
    for k in scoredic:
        if scoredic[k]>max_v:
            max_v=scoredic[k]
            max_k=k
    return max_k
    #return sorted(scoredic,key=scoredic.get)
def score_str_similiarity(s1,s2):
    scores=[]
    for c in s2:
        score=0
        for c2 in s1:
            if c==c2.lower(): score+=1
        scores.append(score)
    return sum(scores)
