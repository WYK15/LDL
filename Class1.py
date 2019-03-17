from functools import reduce


class sensetivor():
    def __init__(self,input_counts,f):
        self.input_counts = input_counts
        self.f = f
        self.bias = 0.0;
        self.weights = [0.0 for _ in range(input_counts)]

    def train(self,inputs,values,times,rate):
        for time in range(times):
            self.iterrator(inputs,values,rate)

    def updatew(self,inputs,value,oldvalue,rate):
        gap =  value - oldvalue
        self.weights = list(map(lambda x,w:w + x * rate * gap,inputs,self.weights))
        self.bias += rate * gap

    def calculate(self,inputs):

         return self.f(reduce(lambda c,d:c+d,list(map(lambda a,b:a*b,inputs,self.weights)),0.0)+self.bias)

    def iterrator(self,inputs,values,rate):
        samples = zip(inputs,values)
        for (v,k) in samples:
            valueold = self.calculate(v)
            self.updatew(v,k,valueold,rate)


def f(x):
    return 1 if x > 0 else 0

def run():
    p = sensetivor(2,f);
    inputs = [[1,1],[0,0],[1,0],[0,1]]
    values = [1,0,0,0]
    p.train(inputs,values,10,0.1)
    return p

if __name__== '__main__':
        cell =  run()
        print(cell.bias)
        print(cell.weights)



