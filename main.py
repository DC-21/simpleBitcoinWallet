#import bitcoin library
from bitcoin import *

#create private key
private_key = random_key()

#create public key
public_key = privtopub(private_key)

#create A Bitcoin Address
Bitcoin_Address = pubtoaddr(public_key)

#print all keys 
print("private key is: " + private_key)
print("public key is: " + public_key)
print("Bitcoin Address is : " + Bitcoin_Address)
