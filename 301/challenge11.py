#!/bin/python3

# Script Name:                  ops301-challenge11
# Author:                       Omar Ardid
# Date of latest revision:      04/08/2024
# Purpose:                      Using Psutil to fetch system information
# Resources:                    https://www.educative.io/answers/what-is-the-psutilcputimes-method-in-python

import psutil 

# Grabs CPU times
cpu_times = psutil.cpu_times()

# Print each component on its own line

# Time spent by normal processes executing in user mode
print(f"Time spent by normal processes executing in user mode: {cpu_times.user}")
print("-" *50)
# Time spent by processes executing in kernel mode
print(f"Time spent by processes executing in kernel mode: {cpu_times.system}")
print("-" *50)
# Time when system was idle
print(f"Time when system was idle: {cpu_times.idle}")
print("-" *50)
# Time spent by priority processes executing in user mode
print(f"Time spent by priority processes executing in user mode: {cpu_times.nice}")
print("-" *50)
# Time spent waiting for I/O to complete.
print(f"Time spent waiting for I/O to complete: {cpu_times.iowait}")
print("-" *50)
# Time spent for servicing hardware interrupts
print(f"Time spent for servicing hardware interrupts: {cpu_times.irq}")
print("-" *50)
# Time spent for servicing software interrupts
print(f"Time spent for servicing software interrupts: {cpu_times.softirq}")
print("-" *50)
# Time spent by other operating systems running in a virtualized environment
print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.steal}")
print("-" *50)
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {cpu_times.guest}")
print("-" *50)