FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model.joblib predict.py example.csv ./

ENTRYPOINT ["python", "predict.py"]
CMD ["example.csv"]
