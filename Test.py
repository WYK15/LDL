from Class1 import sensetivor


def f1(x):
    return 1 if x > 0 else 0

def run1():
    p = sensetivor(2,f1);
    inputs = [[1,1],[0,0],[1,0],[0,1]]
    values = [1,0,0,0]
    p.train(inputs,values,10,0.1)
    return p



def run2():
    f2 = lambda a: a
    p = sensetivor(1,f2)
    inputs = [[5],[3],[8],[1.4],[10.1]]
    values = [5500,2300,7600,1800,11400]
    p.train(inputs,values,10,0.01)
    return p



if __name__== '__main__':
        cell =  run2()
        print(cell.bias)
        print(cell.weights)
        print("3.4 year is %.2f"%cell.calculate([3.4]))


