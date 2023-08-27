FROM python:3.11


RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        git \
        wget \
        vim \
        inetutils-ping net-tools \
        openssh-server \
        sudo \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    true

# Install requirements
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY paratest /paratest

EXPOSE 8501

WORKDIR /

CMD ["python3", "-m", "streamlit", "run", "toughtfusion/webapp/app.py", "--server.port", "8501",
"--browser.gatherUsageStats", "false"]

