FROM python:3.11.2

#Ajeita o fuzo horario para Sao Paulo
COPY --from=tadeorubio/pyodbc-msodbcsql17:latest /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN ln -snf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# Set up Chrome as default browser
ENV BROWSER /usr/bin/chromium

# Copy and install your application dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install necessary dependencies
RUN apt-get update

RUN apt-get install -y chromium

# CHROMIUM default flags for container environnement
# The --no-sandbox flag is needed by default since we execute chromium in a root environnement
RUN echo 'export CHROMIUM_FLAGS="$CHROMIUM_FLAGS --no-sandbox"' >> /etc/chromium.d/default-flags

# MOTD
RUN echo " \n =============HTML2IMAGE============= \n Welcome to the html2image CLI container ! \n Type html2image -h for help :)" >> /etc/motd
RUN echo "clear" >> /root/.bashrc
RUN echo "cat /etc/motd" >> /root/.bashrc

# Copy your application code
COPY . .

CMD ["python", "-u","app.py" ]