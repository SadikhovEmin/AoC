class FileSystem:
    def __init__(self, name, parent):
        self.name = name
        self.val = [0]
        self.nodes = []
        self.parent = parent

    def addFS(self, name, parent):
        self.nodes.append(FileSystem(name, parent))

    def addValue(self, val):
        self.val.append(val)


def getFileSize(s: str) -> int:
    size = ""
    for i in s:
        if i.isnumeric():
            size += i

    return 0 if len(size) == 0 else int(size)


f = open('input.txt')
FS = FileSystem(f.readline().rstrip(), None)

depth = 0

trv = FS
for i in f:
    if "cd /" in i:
        trv = FS
    elif "cd .." in i:
        trv = trv.parent
    elif "cd" in i:
        for j in trv.nodes:
            if j.name in i.replace("cd", ""):
                trv = j
    elif "ls" in i and not i[0].isnumeric():
        continue
    elif "dir" in i:
        trv.addFS(i.strip().lstrip("dir").replace(" ", ""), trv)
    else:
        trv.addValue(getFileSize(i.strip()))

"""
Need to iterate over all of the elements.
Calculate the sum of the files 
if sum <= 10000 then add it and continue with other directories
"""

def directorySize(trv):
    if len(trv.nodes) == 0:
        # sz_ = sum(trv.val)
        # return sz_ if sz_ <= 100000 else 0
        return 0
    sz = 0
    for i in trv.nodes:
        sz += directorySize(i)
        local_files = sum(i.val)
        sz += local_files if local_files <= 100000 else 0

    return sz

trv = FS
size = directorySize(trv)
size += sum(trv.val) if sum(trv.val) <= 100000 else 0
print(size)