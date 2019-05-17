def isfloat(s):
    num=s.partition(".")
    if num[0]=='' and num[2]=='' : return False
    if num[0]!='' and num[2]=='' : return True
    if num[0]=='' and num[2]!='' and num[2]!='.' : return True
    if num[0]!='' and num[2]!='' : return True
    else : return False
print(isfloat(".112"))
print(isfloat("-.112"))
print(isfloat("3.14"))
print(isfloat("-3.14"))
print(isfloat("5."))
print(isfloat("5.0"))
print(isfloat("-777.0"))
print(isfloat("-777."))
print(isfloat("."))
print(isfloat(".."))
