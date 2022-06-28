import matplotlib.pyplot as plt
import numpy as np
import datetime
import math
from numba import jit
import streamlit as st
import pandas as pd

@jit(nopython = True)
def collatz(collatz_num):
    axis_x = []
    axis_y = []
    cnt = 1
    while(collatz_num != 1):
        axis_x.append(cnt)
        axis_y.append(collatz_num)
        if(collatz_num %2 == 0):
            collatz_num //= 2
        else:
            collatz_num = collatz_num*3+1
        
        cnt += 1

    return [axis_x,axis_y]

def list_log(li):
    for i in range(len(li)):
        li[i] = math.log10(li[i])
    return li  
st.header("Collatz conjecture")

string = """The Collatz conjecture is one of the most famous unsolved problems in mathematics.
The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.
It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even,
the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1.
The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.
It is named after mathematician Lothar Collatz, who introduced the idea in 1937, two years after receiving his doctorate.
It is also known as the 3n + 1 problem, the 3n + 1 conjecture, the Ulam conjecture (after Stanisław Ulam), Kakutani's problem (after Shizuo Kakutani),
the Thwaites conjecture (after Sir Bryan Thwaites), Hasse's algorithm (after Helmut Hasse), or the Syracuse problem.
The sequence of numbers involved is sometimes referred to as the hailstone sequence or hailstone numbers
(because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as wondrous numbers."""

st.write(string)
st.empty()
st.latex(r'''f(n) = \begin{cases}
   \frac{n}{2} &\text{if } {n \equiv 0} \pmod 2 \\
   3n+1 &\text{if } {n \equiv 1} \pmod 2
\end{cases}''')
collatz_num = st.number_input('Enter number', min_value = 3, max_value = 10000000000000, value = 3)
collatz_list = collatz(collatz_num)

chart_data = pd.DataFrame(collatz_list[1])
log_chart_data = pd.DataFrame(list_log(collatz_list[1]))
st.subheader("Collatz conjecture chart")
st.line_chart(chart_data)
st.subheader("Collatz conjecture log chart")
st.line_chart(log_chart_data)