# Multithreaded Programming Using Pthreads and OpenMP

## Aim
To develop multithreaded programs using Pthreads and OpenMP and understand thread creation, thread management, work distribution, race conditions, synchronization, and performance improvement.

## Objectives
- Demonstrate Pthread creation, joining, and parallel execution.
- Implement work distribution among multiple threads.
- Expose data inconsistency via race conditions.
- Resolve race conditions using mutex and #pragma omp critical.
- Demonstrate OpenMP barrier synchronization.
- Compare sequential vs Pthreads vs OpenMP performance by calculating speedup and efficiency.

## Environment
- **Operating System:** Windows, WSL Ubuntu
- **Compiler:** GCC
- **Libraries:** POSIX Pthreads, OpenMP
- **Editor/Terminal:** Nano, Terminal

## Experiments
1. **thread1.c**: Creation and joining of one Pthread.
2. **thread2.c**: Multiple Pthreads execution.
3. **thread_sum.c**: Work distribution of an array sum.
4. **race.c**: Pthreads race condition.
5. **mutex.c**: Mutex synchronization.
6. **omp1.c**: OpenMP parallel region.
7. **omp_sum.c**: OpenMP work sharing with reduction.
8. **omp_race.c**: OpenMP race condition.
9. **omp_critical.c**: Critical section synchronization.
10. **omp_barrier.c**: Barrier synchronization.

## Folder Structure
- src/: Source code (.c files)
- data/: Data files
- esults/: CSV performance results
- graphs/: Plotted performance graphs
- screenshots/: Execution output screenshots
- eport/: Laboratory reports
- presentation/: Slides

## Compilation Commands
**Pthreads:**
`ash
gcc thread1.c -o thread1 -pthread
gcc thread2.c -o thread2 -pthread
gcc thread_sum.c -o thread_sum -pthread
gcc race.c -o race -pthread
gcc mutex.c -o mutex -pthread
gcc pthread_perf.c -o pthread_perf -pthread
`

**OpenMP:**
`ash
gcc omp1.c -o omp1 -fopenmp
gcc omp_sum.c -o omp_sum -fopenmp
gcc omp_race.c -o omp_race -fopenmp
gcc omp_critical.c -o omp_critical -fopenmp
gcc omp_barrier.c -o omp_barrier -fopenmp
gcc omp_perf.c -o omp_perf -fopenmp
`

**Sequential:**
`ash
gcc sequential.c -o sequential
`

## Execution Commands
`ash
./thread1
./thread2
./thread_sum
./race
./mutex
./omp1
./omp_sum
./omp_race
./omp_critical
./omp_barrier
./sequential
./pthread_perf
./omp_perf
`

## Performance Results

*Sequential Baseline Execution Time: 1.817299 seconds*

| Threads | Pthreads Time (s) | OpenMP Time (s) |
|---------|-------------------|-----------------|
| 1       | 1.909488          | 1.827057        |
| 2       | 0.980145          | 0.934745        |
| 4       | 0.532650          | 0.501391        |
| 6       | 0.408154          | 0.398321        |
| 16      | 0.256682          | 0.294263        |

## Speedup
*(Formula: Speedup = Sequential Time / Parallel Time)*

| Threads | Pthreads | OpenMP |
|---------|----------|--------|
| 1       | 0.952    | 0.995  |
| 2       | 1.854    | 1.944  |
| 4       | 3.413    | 3.625  |
| 6       | 4.453    | 4.562  |
| 16      | 7.081    | 6.175  |

## Efficiency
*(Formula: Efficiency = (Speedup / Threads) * 100)*

| Threads | Pthreads | OpenMP |
|---------|----------|--------|
| 1       | 95.23%   | 99.47% |
| 2       | 92.71%   | 97.19% |
| 4       | 85.33%   | 90.62% |
| 6       | 74.22%   | 76.04% |
| 16      | 44.26%   | 38.59% |

## Graphs
Graphs illustrating Execution Time vs Number of Threads, Speedup vs Number of Threads, and Efficiency vs Number of Threads can be found in the graphs/ directory.

## Conclusion
This project successfully implemented POSIX Pthreads and OpenMP concepts. Multithreading significantly reduced execution time. We demonstrated that proper synchronization (mutex, critical sections, barriers) is mandatory to prevent data corruption (race conditions), and that parallel efficiency decreases as thread counts scale due to system overhead.
