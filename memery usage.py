import os

import psutil

process = psutil.Process(os.getpid())

print(process.memory_info().rss)