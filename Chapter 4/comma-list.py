def list_join(list):
    output = ''
    for i in range(len(list)):
        if i != (len(list) - 1):
            output += list[i] + ', '
        else:
            output += 'and ' + list[i]
    return output

print(list_join(['a','b','c', 'd']))