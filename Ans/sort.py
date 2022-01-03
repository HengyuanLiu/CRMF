import sys
# prom = "lang"
def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(' ')
                _dict[key] = float(value)
    except IOError as ioerr:
        print "Film  %s doesn't exist" % (filepath)
     
    return _dict
 

if __name__ == '__main__' :
    _dict = load_dict_from_file ('finalAns/'+sys.argv[1]+'/'+sys.argv[1]+sys.argv[2]+'.txt')
    dic1SortList = sorted(_dict.items(), key=lambda dic : dic[1])
    file_handle = open('finalAns/'+sys.argv[1]+'/'+sys.argv[1]+sys.argv[2]+'-ans.txt',mode='w')
    for i in dic1SortList :
	    # print i[1]
	    file_handle.write(i[0])
	    file_handle.write(' ')
	    file_handle.write(str(i[1]))
	    file_handle.write('\n')
    file_handle.close()