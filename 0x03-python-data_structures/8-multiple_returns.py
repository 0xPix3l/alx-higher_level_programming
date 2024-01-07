#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuble = ()
    if len(sentence) == 0:
        my_tuble = (0, None)
    else:
        my_tuble = (len(sentence), sentence[0])
    return my_tuble
        
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))