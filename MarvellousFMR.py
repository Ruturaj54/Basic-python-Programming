def filterx(Task,Elements):
    Result=[]
    for no in Elements:
        if (Task(no)==True):
            Result.append(no)
    return Result

def mapx(Task,Elements):
    Result=[]
    for no in Elements:
        ret=Task(no)
        Result.append(ret)
    return Result

def reducex(Task,Elements):
    Sum=0
    for no in Elements:
        Sum=Task(Sum,no)
        
    return Sum    