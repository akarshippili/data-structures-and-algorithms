class StockSpanner:

    def __init__(self):
        self.arr=[]
        self.count = 0

    def next(self, price: int) -> int:
        self.count += 1
        
        while(self.arr and self.arr[-1][0]<=price): self.arr.pop()
        self.arr.append([price, self.count])
        
        # print(self. count, self.arr)
        
        return self.count - self.arr[-2][1]  if(len(self.arr)>=2) else self.count
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
