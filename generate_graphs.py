import os
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))

# Data
threads = [1, 2, 4, 6, 16]
seq_time = [1.817299] * len(threads)

p_time = [1.909488, 0.980145, 0.532650, 0.408154, 0.256682]
omp_time = [1.827057, 0.934745, 0.501391, 0.398321, 0.294263]

p_speedup = [0.952, 1.854, 3.413, 4.453, 7.081]
omp_speedup = [0.995, 1.944, 3.625, 4.562, 6.175]

p_eff = [95.23, 92.71, 85.33, 74.22, 44.26]
omp_eff = [99.47, 97.19, 90.62, 76.04, 38.59]

graphs_dir = os.path.join(base_dir, 'graphs')
os.makedirs(graphs_dir, exist_ok=True)

# 1. Execution Time Graph
plt.figure(figsize=(10, 6))
plt.plot(threads, seq_time, label='Sequential Baseline', linestyle='--', marker='x', color='red')
plt.plot(threads, p_time, label='Pthreads', marker='o', color='blue')
plt.plot(threads, omp_time, label='OpenMP', marker='s', color='green')
plt.title('Execution Time vs Number of Threads')
plt.xlabel('Number of Threads')
plt.ylabel('Execution Time (seconds)')
plt.xticks(threads)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.savefig(os.path.join(graphs_dir, 'execution_time.png'))
plt.close()

# 2. Speedup Graph
plt.figure(figsize=(10, 6))
plt.plot(threads, p_speedup, label='Pthreads', marker='o', color='blue')
plt.plot(threads, omp_speedup, label='OpenMP', marker='s', color='green')
plt.title('Speedup vs Number of Threads')
plt.xlabel('Number of Threads')
plt.ylabel('Speedup')
plt.xticks(threads)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.savefig(os.path.join(graphs_dir, 'speedup.png'))
plt.close()

# 3. Efficiency Graph
plt.figure(figsize=(10, 6))
plt.plot(threads, p_eff, label='Pthreads', marker='o', color='blue')
plt.plot(threads, omp_eff, label='OpenMP', marker='s', color='green')
plt.title('Efficiency vs Number of Threads')
plt.xlabel('Number of Threads')
plt.ylabel('Efficiency (%)')
plt.xticks(threads)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.savefig(os.path.join(graphs_dir, 'efficiency.png'))
plt.close()

print(f"Graphs successfully generated in: {graphs_dir}")
