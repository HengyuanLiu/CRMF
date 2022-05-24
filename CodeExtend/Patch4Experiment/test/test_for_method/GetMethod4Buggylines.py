import os
import javalang
import pandas as pd

def get_token_frame(java_src):
    tokens = javalang.tokenizer.tokenize(java_src)
    t_list = []
    t_dict = {
        "type": [],
        "value": [],
        "lineNum": [],
        "colNum": []
    }

    for each_t in tokens:
        t_dict["type"] = type(each_t).__name__
        t_dict["value"] = each_t.value
        t_dict["lineNum"] = each_t.position[0]
        t_dict["colNum"] = each_t.position[1]
        t_list.append(t_dict.copy())

    t_df = pd.DataFrame(t_list)
    return t_df


def get_code_entity_scope(node_type, code_tree, t_df):
    """
    get all entity scope match node_type
    :param node_type: javalang.tree.nodeType [javalang.tree.MethodDeclaration, javalang.tree.ClassDeclaration]
    :param code_tree: codeTree generated by javalang parser
    :param t_df: token dataframe
    :return: code_entity_scope [pd.DataFrame]
    """
    tf_separator_df = t_df[t_df["type"] == "Separator"]
    code_entity_scope = []
    for _, node in code_tree.filter(node_type):
        entity_name = node.name
        entity_lineNum = node.position[0]
        entity_colNum = node.position[1]

        depth = 0
        for t_i in tf_separator_df.index:
            if tf_separator_df.loc[t_i, "lineNum"] > entity_lineNum or (tf_separator_df.loc[t_i, "lineNum"] == entity_lineNum and tf_separator_df.loc[t_i, "colNum"] >= entity_colNum):
                if tf_separator_df.loc[t_i, "value"] == "{":  # and tf_separator_df.loc[t_i, "type"] == "Separator":
                    depth += 1

                if tf_separator_df.loc[t_i, "value"] == "}":  # and tf_separator_df.loc[t_i, "type"] == "Separator":
                    depth -= 1
                    if depth == 0:
                        break

        entity_startine = entity_lineNum
        entity_endline = t_df.loc[t_i, "lineNum"]

        code_entity_scope.append({"entity_name": entity_name, "entity_scope": (entity_startine, entity_endline)})
    return code_entity_scope


fp = open("./buggy_lines.txt", mode="r", encoding="UTF-8")
buggy_lines = fp.read()
fp.close()
buggy_lines = buggy_lines.strip().split("\n")
buggy_files = list(set([buggy_line.split('#')[0] for buggy_line in buggy_lines])) 

src_path = "../../gson/src/main/java"

methodsScope4BuggyFile = {}

# for buggy_file in buggy_files:
#     print(os.path.join(src_path, buggy_file))
#     fp = open(os.path.join(src_path, buggy_file), mode="r", encoding="UTF-8")
#     java_str = fp.read()
#     fp.close()

#     tokens = javalang.tokenizer.tokenize(java_str)
#     tree = javalang.parse.parse(java_str)  # 根据源代码解析出一颗抽象语法树

#     t_df = get_token_frame(java_str)

#     print("----------------METHOD------------------")
#     methodsScope = get_code_entity_scope(javalang.tree.MethodDeclaration, tree, t_df)
#     for methodScope in methodsScope:
#         print(methodScope["entity_name"], ":", methodScope["entity_scope"])

#     print("----------------CLASS------------------")
#     classesScope = get_code_entity_scope(javalang.tree.ClassDeclaration, tree, t_df)
#     for classScope in classesScope:
#         print(classScope["entity_name"], ":", classScope["entity_scope"])

#     print("------------METHOD NAME----------------")
#     methodNames = []
#     if classesScope:
#         class_prefix = buggy_file.strip().split('.')[0]
#         class_prefix = class_prefix.replace('/', '.').strip().split('.')[:-1]
#         for classScope in classesScope:
#             for methodScope in methodsScope:
#                 if classScope["entity_scope"][0] <= methodScope["entity_scope"][0] and methodScope["entity_scope"][1] <= classScope["entity_scope"][1]:
#                     methodName = '.'.join(class_prefix + [classScope["entity_name"], methodScope["entity_name"]])
#                     methodNames.append(methodName)
#     else:
#         class_prefix = buggy_file.strip().split('.')[0]
#         class_prefix = class_prefix.replace('/', '.').strip().split('.')
#         for methodScope in methodsScope:
#             methodName = '.'.join(class_prefix + [methodScope["entity_name"]])
#             methodNames.append(methodName)

#     for methodName in methodNames:
#         print(methodName)

AllBuggyMethod = []
for buggy_line in buggy_lines:
    buggy_file = buggy_line.split('#')[0]
    buggy_lineNum = int(buggy_line.split('#')[1])

    # print(os.path.join(src_path, buggy_file))
    fp = open(os.path.join(src_path, buggy_file), mode="r", encoding="UTF-8")
    java_str = fp.read()
    fp.close()

    tokens = javalang.tokenizer.tokenize(java_str)
    tree = javalang.parse.parse(java_str)  # 根据源代码解析出一颗抽象语法树

    t_df = get_token_frame(java_str)

    # print("----------------METHOD------------------")
    methodsScope = get_code_entity_scope(javalang.tree.MethodDeclaration, tree, t_df)
    # for methodScope in methodsScope:
        # print(methodScope["entity_name"], ":", methodScope["entity_scope"])

    # print("----------------CLASS------------------")
    classesScope = get_code_entity_scope(javalang.tree.ClassDeclaration, tree, t_df)
    # for classScope in classesScope:
        # print(classScope["entity_name"], ":", classScope["entity_scope"])

    # print("-----------BUGGY METHOD NAME------------")
    buggymethodNames = []
    if classesScope:
        class_prefix = buggy_file.strip().split('.')[0]
        class_name = class_prefix.replace('/', '.').strip().split('.')[-1]
        class_prefix = class_prefix.replace('/', '.').strip().split('.')
        for methodScope in methodsScope:
            classCandidatesDis = []
            classCandidatesScope = [] 
            for classScope in classesScope:
                if classScope["entity_scope"][0] <= buggy_lineNum <= classScope["entity_scope"][1]:
                    if classScope["entity_scope"][0] <= methodScope["entity_scope"][0] and methodScope["entity_scope"][1] <= classScope["entity_scope"][1]:
                        classCandidatesDis.append((methodScope["entity_scope"][0] - classScope["entity_scope"][0]) + (classScope["entity_scope"][1] - methodScope["entity_scope"][1]))
                        classCandidatesScope.append(classScope)
            if classCandidatesDis:
                classCandidateIndex = classCandidatesDis.index(min(classCandidatesDis))
                classScope = classCandidatesScope[classCandidateIndex]
                if methodScope["entity_scope"][0] <= buggy_lineNum <= methodScope["entity_scope"][1]:
                    if classScope["entity_name"] == class_name:
                        buggymethodName = '.'.join(class_prefix + [methodScope["entity_name"]])
                        buggymethodNames.append(buggymethodName)
                    else:
                        buggymethodName = '.'.join(class_prefix) + '$' + '.'.join([classScope["entity_name"], methodScope["entity_name"]])
                        buggymethodNames.append(buggymethodName)
    else:
        class_prefix = buggy_file.strip().split('.')[0]
        class_prefix = class_prefix.replace('/', '.').strip().split('.')
        for methodScope in methodsScope:
            if methodScope["entity_scope"][0] <= buggy_lineNum <= methodScope["entity_scope"][1]:
                buggymethodName = '.'.join(class_prefix + [methodScope["entity_name"]])
                buggymethodNames.append(buggymethodName)

    # for buggymethodName in buggymethodNames:
    #     print(buggymethodName)
    
    AllBuggyMethod.extend(buggymethodNames)

AllBuggyMethod = list(set(AllBuggyMethod))

# for buggymethodName in AllBuggyMethod:
#     print(buggymethodName)

fp = open("./buggy_methods.txt", mode='w')
fp.write('\n'.join(AllBuggyMethod))
fp.close()