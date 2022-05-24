fp=open("./all_methods.txt",mode='r')
all_methods = fp.readlines()
fp.close()

fp=open("../test_for_class/covfclasses.txt",mode='r')
covf_classes = fp.readlines()
fp.close()

def JudgeCovf(method, covf_classes):
    flag = False
    for c in covf_classes:
        if c.strip() in method.strip():
            flag = True
            break
    return flag

covf_methods = [method for method in all_methods if JudgeCovf(method, covf_classes)]

fp=open("./covf_methods.txt",mode='w')
fp.write(''.join(covf_methods))
fp.close()