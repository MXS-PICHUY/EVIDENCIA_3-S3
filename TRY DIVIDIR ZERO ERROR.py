a=10
b=1

try:
    c=b/a
    print(c)
except(IOError,ZeroDivisionError) as x:
    print('error',x)
else:
    print('no error')
    
print('fiinnn deeel prrrooogggrammmaaaaaaa.....')