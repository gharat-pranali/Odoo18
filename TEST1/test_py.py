import requests
import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import random, string, base64
key='Xn2RUnszSmNFNYYq'.encode('utf-8')
enc_s = AES.new(key, AES.MODE_ECB)
data={'fname': 'shazz', 'lname': '', 'company': 'ABC', 'email': 'srpod@sanraj.com', 'query': 'Test Lead Ignore', 'phone': '917709845260', 'product': 'RML Messaging,RML Voice', 'domainname': 'routemobile.com', 'clientip': '59.152.53.50', 'country': 'India', 'source_id': 'Facebook', 'other': ''}
json_str = json.dumps(data)

#data="this is a super important message"
byte_data = json_str.encode('utf-8')  
padded_data = pad(byte_data, AES.block_size)

cipher_text = enc_s.encrypt(padded_data)
print("cipher_text",cipher_text)
encoded_cipher_text = base64.b64encode(cipher_text)
print("encoded_cipher_text",encoded_cipher_text)
#data={'payload':{'fname': 'shazz', 'lname': 'wazz', 'company': 'ABC', 'email': 'srpod@sanraj.com', 'query': 'Test Lead Ignore', 'phone': '917709845260', 'product': 'RML Messaging,RML Voice', 'domainname': 'routemobile.com', 'clientip': #'59.152.53.50', 'country': 'India', 'source_id': 'Facebook', 'other': ''}}
#print("data",data)
#url = 'http://localhost:1818//rmlwebsitelead/create/v1/'
#header = {'Api-Key' : 'wZW5kaW5nJywgJ2lzX2xpdmUnOiBUcnV'}
res = requests.post(url, headers = header,data=data)
print("res11111111",res.text)
