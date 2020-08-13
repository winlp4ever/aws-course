import json
import re
import numpy as np
from utils import foo

def main(event, context):
    a = np.array([1, 2, 3])
    foo()
    return {
        "array": a.tolist(),
        "status": "ok"
    }

if __name__ == "__main__":
    main('', '')