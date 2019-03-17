from Class1 import sensetivor


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


