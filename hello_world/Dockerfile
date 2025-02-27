FROM public.ecr.aws/lambda/python:3.10

# python path에 /opt 지정
ENV PYTHONPATH="/opt:${PYTHONPATH}"

# 작업 디렉토리 설정
WORKDIR /var/task

# 패키지 설치
COPY requirements.txt ./
RUN python3.10 -m pip install -r requirements.txt

# Layer 복사
COPY layers/my-layer/python /opt

# Lambda 핸들러 복사
COPY app.py ./

# Lambda 실행 명령
CMD ["app.lambda_handler"]