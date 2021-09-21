# A Dockerfile is used to define how your code will be packaged. This includes
# your code, the base image and any additional dependencies you need.
FROM python:3.8

# Now we include the Python requirements.txt file and install any missing dependencies.
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Finally, we include our code and specify what command should be run to execute it.
COPY main.py .
COPY test.py .
COPY test.jpg .

ENV PATH="/:${PATH}"
CMD ["main.py"]
