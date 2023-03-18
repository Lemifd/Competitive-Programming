class Solution:
    def intToRoman(self, num: int) -> str:

        roman={"1000":"M","5":"D","10":"C","50":"L","10":"X","5":"V","1":"I"}
        array=[]
        for i in str(num):
            array.append(int(i))
     
        ans=""
        for i in range(len(array)-1,-1,-1):
            if i==0:
                if array[i]<4:
                    k='I'*array[i]
                elif array[i]==4:
                    k="IV"
                elif array[i]==9:
                    k="IX"
                else:
                    k="V"+"I"*(array[i]-5)
            if i==1:
                if array[i]<4:
                    k='X'*array[i]
                elif array[i]==4:
                    k="XL"
                elif array[i]==9:
                    k="XC"
                else:
                    k="L"
            if i==2:
                if array[i]<4:
                    k='C'*array[i]
                elif array[i]==4:
                    k="CD"
                elif array[i]==9:
                    k="CM"
                else:
                    k="C"
            if i==3:
                if array[i]<4:
                    k='M'*array[i]
            print(k)
            
            ans=k+ans
            return ans
    

num=123
print(Solution().intToRoman(num))