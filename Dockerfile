FROM python:3.10

WORKDIR /app

# system deps
RUN apt update && apt install -y iputils-ping vim && rm -rf /var/lib/apt/lists/*
#add commit to check 'git branch -d develop && git push origin --delete develop'
# python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app code
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

