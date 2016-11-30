__author__ = 'วรรณพงษ์'
#import re
print("Text")
a = input("Text")
if a.find("+"):
    s = a.split("+")
    in1 = int(s[0])
    in2 = int(s[1])
    cal = in1 + in2
elif a.find("-"):
    s = a.split("-")
    in1 = int(s[0])
    in2 = int(s[1])
    cal = in1 - in2
elif a.find("*"):
    s = a.split("*")
    in1 = int(s[0])
    in2 = int(s[1])
    cal = in1 * in2
elif a.find("//"):
    s = a.split("//")
    in1 = int(s[0])
    in2 = int(s[1])
    cal = in1 // in2
else:
    cal = "error";
print(cal)
