# Parallel Computing Presentation

## Slide 1: Title
- **Title:** Multithreaded Programming Using Pthreads and OpenMP
- **Subtitle:** Parallel Computing Laboratory Project

## Slide 2: Aim and Objectives
- Develop multithreaded programs using Pthreads and OpenMP.
- Demonstrate thread creation, joining, and work distribution.
- Identify and handle race conditions using mutexes and critical sections.
- Analyze execution time, speedup, and efficiency.

## Slide 3: Environment
- **Operating System:** Windows, WSL Ubuntu
- **Compiler:** GCC
- **Libraries:** POSIX Pthreads, OpenMP
- **Tools:** Nano, Terminal

## Slide 4: Pthreads
- POSIX Threads (Pthreads) allows explicit management of threads.
- `thread1.c` & `thread2.c`: Demonstrated thread creation using `pthread_create()` and joining using `pthread_join()`. Thread execution order depends on OS scheduling.

## Slide 5: Thread Creation and Work Distribution
- **Work Distribution:** `thread_sum.c` divided an 8-element array evenly across 4 threads. 
- Each thread calculated a partial sum (30, 70, 110, 150).
- The main thread successfully accumulated them to a total of 360.

## Slide 6: Race Condition and Mutex
- **Race Condition (`race.c`):** 4 threads executing 100,000 increments resulted in data loss (135,420 instead of 400,000).
- **Mutex Fixed (`mutex.c`):** Using `pthread_mutex_lock()` and `pthread_mutex_unlock()` ensured safe memory access, correctly outputting 400,000.

## Slide 7: OpenMP
- OpenMP enables compiler-directed, high-level multithreading via `#pragma` directives.
- `omp1.c`: Showed implicit parallel region execution, confirming 16 threads actively executed the block.

## Slide 8: Race Condition, Critical and Barrier
- **OpenMP Race (`omp_race.c`):** Produced 101,499 instead of 400,000.
- **Critical Section (`omp_critical.c`):** Using `#pragma omp critical` safely achieved 400,000.
- **Barrier (`omp_barrier.c`):** Using `#pragma omp barrier` synchronized all threads at Stage 1 before allowing any to enter Stage 2.

## Slide 9: Performance Experiment
- **Workload:** 1,000,000,000 iterations computing a sum of 499999999500.00.
- **Sequential Baseline:** Completed in 1.817299 seconds.
- Ran tests iteratively with 1, 2, 4, 6, and 16 threads using both Pthreads and OpenMP.

## Slide 10: Results and Graphs
- **Pthreads (16 threads):** 0.256682 seconds (7.081x Speedup)
- **OpenMP (16 threads):** 0.294263 seconds (6.175x Speedup)
- [Insert Graphs: Execution Time, Speedup, Efficiency]

## Slide 11: Observations
- Adding threads significantly drops execution time.
- However, Speedup is non-linear. 16 threads do not provide 16x speedup.
- Efficiency drops sharply at 16 threads (Pthreads: 44.26%, OpenMP: 38.59%) due to overhead such as scheduling and context switching.

## Slide 12: Conclusion
- Pthreads provides fine-grained explicit control, while OpenMP simplifies data parallelism.
- Synchronization is strictly necessary to prevent race conditions but introduces latency.
- Parallel programming dramatically improves workload execution but has an upper limit defined by Amdahl's Law and system overhead.
