import json
import debugpy

# 디버거 연결 대기
debugpy.listen(("0.0.0.0", 5890))
print("Waiting for debugger to attach...")
debugpy.wait_for_client()  # 디버거가 연결될 때까지 대기

def lambda_handler(event, context):
    """
    Sample pure Lambda function
    """
    debugpy.breakpoint()
    
    import numpy as np
    
    print("디버깅 시작!")
    a = 'aaa'
    print('Break point 1')
    print(a)
    print('Break point 2')
    
    
    
    print(f'np version: {np.__version__}')
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Success"
            }
        ),
    }
