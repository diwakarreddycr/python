class array:
    def input():
        arr=[]
        size=int(input("Enter the size of an array:"))
        for i in range(size):
            a=i+1
            element = int(input("Enter the element of [%d]:"%a))
            arr.append(element)
        return arr
            
    def desc(arr):
        temp=0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]<arr[j]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        return arr
    def asce(arr):
        temp=0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        return arr
