# python image
FROM python:3.13-slim

# work directory
WORKDIR /app

# libraries installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy complete code
COPY . .

# give port
EXPOSE 8000

# start!
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
