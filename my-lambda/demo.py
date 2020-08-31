from support import pr

import numpy as np

def main(event, context):
    print(np.array([1, 2, 4]))
    return {
        "status": 200,
        "msg": pr()
    }

if __name__ == '__main__':
    main({}, {})
