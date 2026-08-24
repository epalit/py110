
## Notes on pdb

- In-built Python debugger
- From Python 3.13, `pdb.set_trace()` pauses the program **on the line where it is called** (not the next line to be executed)

### How to start it

- put breakpoints directly in the code (can set multiple breakpoints with `set_trace`):

```python
import pdb

# code here
pdb.set_trace() # adds breakpoint
```

- run on the command line:
```python
python -m pdb your_file.py
```

### pdb commands
- `p <variable_name>` outputs the value of the variable
- `c` executes code until the next breakpoint (continue)
- `n` move to next line (steps over/through functions i.e. executes it)
- `q + enter`, `quit + enter`, `exit + enter` exit
- `b` set breakpoint at a specific line e.g. `b 6`
  - breakpoints are assigned incremental numbers
- `cl 1` or `clear 1` removes the first breakpoint
  - ```(Pdb) b 6
    Breakpoint 1 at /Users/xyzzy/ls_test/test.py(6)
    (Pdb) cl 1
    Deleted breakpoint 1 at /Users/xyzzy/ls_test/test.py(6)
    ```
- `s` steps into functions
- `r` runs the program until the current function returns
- `help` displays an overview of available commands
- `list` displays 11 lines of source code: 5 lines before the current line, the current line itself, and 5 lines after the current line. Specify a starting and ending line number, e.g., list 10,20 to display lines 10 through 20 (inclusive)
- `where` displays a stack trace that shows how you got to your current position in the code. The most recent function call appears at the bottom, while the topmost entry shows where execution started

### next/step/return
- Use next to step over (or through) functions and move to the next line after the function.
- Use step to step into a function and inspect its behavior line-by-line.
- Use return to quickly exit a function you've stepped into.
