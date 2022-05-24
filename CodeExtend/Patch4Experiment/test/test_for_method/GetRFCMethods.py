fp=open("./all_methods.txt",mode='r')
all_methods = fp.readlines()
fp.close()

fp=open("../test_for_RFC/RFC_classes.txt",mode='r')
RFC_classes = fp.readlines()
fp.close()

def JudgeRFC(method, RFC_classes):
    flag = False
    for c in RFC_classes:
        if c.strip() in method.strip():
            flag = True
            break
    return flag

RFC_methods = [method for method in all_methods if JudgeRFC(method, RFC_classes)]

fp=open("./RFC_methods.txt",mode='w')
fp.write(''.join(RFC_methods))
fp.close()