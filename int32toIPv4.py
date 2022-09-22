import re

def int32_to_ip(int32):

    bin_list = re.findall('........', "{:032b}".format(int32))
    convert = []
    for eachnum in bin_list:
      convert.append(str(int(eachnum, 2)))
    result = ('.'.join(convert))
    return(result)

int32_to_ip(2112585105)

RESULT = 125.235.125.145
