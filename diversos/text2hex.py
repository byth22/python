#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Text 2 Hex, written by byth22
from sys import stdout
from re import sub
from sys import argv
from os import system

def banner():
    print""
    print""
    print("\t================")
    print("\t -- Text2Hex -- ")
    print("\t================")
    print("\t================")
    print""
    print""

    return 0

def limpar():
    system('clear')
    return 0

def entrada():
    text=str(argv[1])
    return text

def process(arg0):
    stdout.write("[+] Saída: ")
    for i in arg0:
        stdout.write("\\")
        stdout.write(sub("0", "", str(hex(ord(i)))))

    stdout.write("\n")
    stdout.write("\n")
    return 0

limpar()

banner()

if (len(argv) != 2):
    print ("\t[-] Número de argumentos não corresponde!")
    print ("\t[*] Usage:")
    print ("\t\t[+] text2hex.py + String")
    exit()

process(entrada())
