#!/bin/python3

import psutil

# CPU Time
print(f"CPU Time: {psutil.cpu_times()}\n")
print(f"CPU Consumption: {psutil.cpu_percent}\n")
print(f"CPU Temperature: {psutil.sensors_temperatures}\n")