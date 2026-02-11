
import sys
import os
sys.path.append(os.getcwd())

try:
    import src.data.feeder
    print("SUCCESS: src.data.feeder imported.")
except Exception as e:
    import traceback
    traceback.print_exc()
