from random import randint
from math import gcd
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
#from qiskit.aqua.algorithms import Shor

def shor_algorithm(N):
    # 检查输入是否大于2
    if  N <= 2:
        raise ValueError("N必须大于2")

    # 初始化量子电路
    qc = QuantumCircuit(3, 3)

    # 添加Hadamard门到第一个量子比特
    qc.h(0)

    # 添加控制NOT门
    qc.cx(0, 1)
    qc.cx(1, 2)

    # 添加Hadamard门到第二个量子比特
    qc.h(1)

    # 测量结果
    qc.measure([0, 1, 2], [0, 1, 2])

    # 使用Aer模拟器运行量子电路
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit).result()
    counts = result.get_counts()

    # 计算r
    r = int(list(counts.keys())[0], 2)

    # 检查r是否满足条件
    if r % 2 == 0 and (pow(r, N, N) - 1) % N == 0:
        return gcd(r, N)
    else:
        return None

def main():
    N = randint(1, 2000)
    #N=1517
    print("输入整数为：", N)
    factors = []
    while True:
        A = randint(1, N - 1)
        gcd_value = gcd(A, N)
        if gcd_value != 1:
            #print("随机生成的在1-N之间的整数为：", A)
            factors.append(gcd_value)
        else:
            factor = shor_algorithm(N)
            if factor is not None:
                #print("随机生成的在1-N之间的整数为：", A)
                factors.append(factor)
        if len(factors) == 2:
            break

    print("素数因子：", factors)

if __name__ == "__main__":
    main()
