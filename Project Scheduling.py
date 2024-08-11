class Task:
    def __init__(self, n, d, deps=None):
        self.n = n
        self.d = d
        self.deps = deps if deps else []
        self.est = 0
        self.eft = 0
        self.lft = float('inf')
        self.lst = float('inf')
#Calculation for EFT AND EST
def fwd_pass(tasks):
    for t in tasks:
        if t.deps:
            t.est = max(dep.eft for dep in t.deps)
        else:
            t.est = 0
        t.eft = t.est + t.d
#Calculation for LFT AND LST
def bwd_pass(tasks, comp_time):
    for t in tasks:
        if not any(t in succ.deps for succ in tasks):
            t.lft = comp_time

    for t in reversed(tasks):
        if not any(t in succ.deps for succ in tasks):
            t.lft = comp_time
        else:
            t.lft = min(succ.lst for succ in tasks if t in succ.deps)
        t.lst = t.lft - t.d

def calc_proj_times(tasks, deadline):
    fwd_pass(tasks)
    earliest_comp = max(t.eft for t in tasks)
    comp_time = max(earliest_comp, deadline)
    bwd_pass(tasks, comp_time)

    return earliest_comp, comp_time

def print_times(earliest, latest):
    print(f"Earliest completion: {earliest}")
    print(f"Latest completion: {latest}")

def main():
    taskA = Task('A', 2)
    taskB = Task('B', 1, [taskA])
    taskC = Task('C', 3, [taskA])
    taskD = Task('D', 1, [taskB])
    taskE = Task('E', 2, [taskD])
    taskF = Task('F', 1, [taskC, taskE])

    tasks = [taskA, taskB, taskC, taskD, taskE, taskF]
    deadline = 10

    earliest, latest = calc_proj_times(tasks, deadline)
    print_times(earliest, latest)

if __name__ == "__main__":
    main()
