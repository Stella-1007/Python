p = int(input("입력 진수 결정(16/10/8/2):"))
v = input("값 입력:")

if(p == 16):
    dval = int(v,16)
if(p == 10):
    dval = int(v, 10)
if(p == 8):
    dval = int(v, 8)
if(p == 2):
    dval = int(v, 2)
    

print("16진수 ==> ",hex(dval))
print("10진수 ==> ",dval)
print("8진수 ==> ", oct(dval))
print("2진수 ==> ", bin(dval))
