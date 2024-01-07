def no_c(mystring):
    new_string = mystring.translate({ord(i): None for i in 'cC'})
    return new_string

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))