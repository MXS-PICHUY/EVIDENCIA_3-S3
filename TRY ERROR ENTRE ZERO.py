try:
    print(5/0)
except(TypeError,ZeroDivisionError) as e:
    
    print('error',e)
else:
    print(5/0)
    
print('fiinnn deeel prrrooogggrammmaaaaaaa.....')