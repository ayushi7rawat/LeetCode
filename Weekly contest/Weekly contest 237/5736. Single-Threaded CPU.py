'''
5736. Single-Threaded CPU
Author: Ayushi Rawat

You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.
You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

Constraints:
tasks.length == n
1 <= n <= 105
1 <= enqueueTimei, processingTimei <= 109
'''

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=[ (ent,pt,i) for i,(ent,pt) in enumerate(tasks)]
        tasks.sort()
        #print(tasks)
        heap=[]
        #t=tasks[0][0]
        i=0
        Ans=[]
        t=0
        while(i<len(tasks)):
            #print("t:{}".format(t))
            
            
            while(i<len(tasks) and tasks[i][0]<=t):
                ent,pt,ind=tasks[i]
                i+=1
                heapq.heappush(heap,(pt,ind))
            
            if len(heap)==0:
                if i<len(tasks):
                    t=tasks[i][0]
                continue
            
            #if len(heap)
            
            pt,ind=heapq.heappop(heap)
            #print("Adding ind:{} at t:{}".format(ind,t))
            Ans.append(ind)
            t+=pt
        while(len(heap)):
            pt,index1=heapq.heappop(heap)
            Ans.append(index1)
        return Ans