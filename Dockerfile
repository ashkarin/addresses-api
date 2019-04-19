FROM ubuntu:18.04

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

# configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV INSTALLER Miniconda3-latest-Linux-x86_64.sh

# Install conda with python 3.7
RUN cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    echo $(wget --quiet -O - https://repo.continuum.io/miniconda/ \
       | grep -A3 $INSTALLER \
       | tail -n1 \
       | cut -d\> -f2 \
       | cut -d\< -f1 ) $INSTALLER | md5sum -c - && \
    /bin/sh $INSTALLER -f -b -p $CONDA_DIR && \
    rm $INSTALLER

RUN conda install -y pandas numpy sqlalchemy flask matplotlib psycopg2 pil yaml
#RUN pip install pyyaml flask_script flask_sqlalchemy
# Set apps working directory
WORKDIR /app

# Copy the local files to the container's workspace
ADD /project /app

# Install rest of packages
RUN cd /app && pip install -r requirements.txt

# Set entrypoint
RUN echo '#!/bin/sh\n\
cd /app\n\
python manage.py export --path /app/assets/Adressen__Berlin.csv --conf /app/assets/columns_config.yaml\n\
echo "EXPORT COMPLETED"\n\
python manage.py run\n\
' > /app/entry.sh && chmod +x /app/entry.sh

ENTRYPOINT /app/entry.sh

EXPOSE 80 8080