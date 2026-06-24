"""
CodeToAGI — Episode 48 Challenge Solution
Compare slow vs fast implementation + full profiling demo
"""

import timeit
import cProfile
import pstats
from pstats import SortKey

# ========================================
# 1. SLOW vs FAST Implementation
# ========================================

def slow_string_build(n=1000):
    """Slow way: repeated string concatenation"""
    result = ""
    for i in range(n):
        result += str(i) + " "
    return result.strip()


def fast_string_build(n=1000):
    """Fast way: using list + join"""
    result = []
    for i in range(n):
        result.append(str(i))
    return " ".join(result)


# ========================================
# 2. Timeit Comparison
# ========================================

print("=== TIMEIT COMPARISON (10,000 runs) ===\n")

slow_time = timeit.timeit(lambda: slow_string_build(1000), number=10000)
fast_time = timeit.timeit(lambda: fast_string_build(1000), number=10000)

print(f"Slow version (string +=):  {slow_time:.4f} seconds")
print(f"Fast version (list + join): {fast_time:.4f} seconds")
print(f"Speedup: {slow_time / fast_time:.1f}x faster!\n")


# ========================================
# 3. cProfile on a small pipeline
# ========================================

def pipeline():
    data = [f"  Item {i}   " for i in range(50_000)]
    cleaned = slow_string_build(5000)  # bottleneck
    processed = [x.strip().upper() for x in data]
    return len(cleaned), len(processed)


print("=== CPROFILE REPORT ===")
cProfile.run('pipeline()', sort=SortKey.CUMULATIVE)


# ========================================
# 4. BONUS: How to use line_profiler
# ========================================

"""
BONUS: line_profiler

1. pip install line_profiler
2. Add @profile decorator:

@profile
def slow_function():
    ...

3. Run:
   kernprof -l -v challenge_solution.py
"""

print("\n✅ Challenge Complete!")
print("Try modifying the slow function and re-measure!")
