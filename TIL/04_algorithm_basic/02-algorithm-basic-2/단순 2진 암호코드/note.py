temp = '0000000110010100011010001101011110110111001001100100110111011000000000'

print(temp.rfind('1'))

finish_index = temp.rfind('1')+1
start_index = finish_index-56
print(start_index, finish_index)
print(len(temp[start_index:finish_index]))
