# Results Summary

## Summary of Correctness
All computational experiments executed correctly. The performance executions across Pthreads and OpenMP reliably returned the expected sum: 499999999500.00. 
Race conditions correctly resulted in unexpected data corruption (135420 and 101499 respectively), which was successfully mitigated back to 400000 via synchronization.

## Highlights
- **Best Pthreads Performance:** 16 threads (0.256682 seconds, 7.081 Speedup)
- **Best OpenMP Performance:** 16 threads (0.294263 seconds, 6.175 Speedup)
- **Highest Efficiency:** 1 thread OpenMP (99.47%)
