# Episode 48 — Profiling & Performance

**Stop Guessing Why Your Code Is Slow — Profile It Instead**

Learn how to use Python's most powerful profiling tools to find real bottlenecks.

## 📁 Files

- `challenge_solution.py` — Complete solution for the YouTube challenge
- `optimize_workflow.py` — Mini project shown in the video
- `timeit_basics.py`, `cprofile_basics.py`, etc. — Code examples from the episode

## 🎯 Challenge (from the video)

Compare two implementations of the same function using `timeit`, then profile with `cProfile` and (bonus) `line_profiler`.

**Solution file**: [`challenge_solution.py`](challenge_solution.py)

## How to Run

```bash
# 1. Create virtual environment (recommended)
python -m venv myenv
myenv\Scripts\activate    # Windows
# source myenv/bin/activate  # Linux/Mac

# 2. Install dependencies
pip install line_profiler  # for bonus

# 3. Run the challenge solution
python challenge_solution.py
