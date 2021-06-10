FROM waggle/plugin-base:1.1.0-ml-cuda11.0-amd64

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3" , "main.py"]
