#!/usr/bin/python

import getpass
import sys
import telnetlib

HOST = "192.168.255.10"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until('Username: ')
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("en\n")
tn.write("Ciscoadmin123!\n")

tn.write("config t\n")
tn.write("int lo0\n")
tn.write("ip addr 2.2.2.2 255.255.255.255\n")

tn.write("end\n")
tn.write("show ip interface brief\n")
tn.write("exit\n")

print(tn.read_all())
