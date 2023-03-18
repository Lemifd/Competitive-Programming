class Solution:
    def average(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))
        sum=0
        for i in salary:
            sum=sum+i
        return sum/len(salary)

salary = [4000,3000,1000,2000]

print(Solution().average(salary))