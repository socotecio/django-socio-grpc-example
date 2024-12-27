FROM python:3.12

ENV PYTHONUNBUFFERED 1 

WORKDIR /opt/code

RUN apt-get update \
    && apt-get install curl locales -y \
    && curl -sSL https://install.python-poetry.org | python -

RUN sed -i 's/^# *\(fr_FR.UTF-8\)/\1/' /etc/locale.gen
RUN sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen
RUN locale-gen

ENV PATH="/root/.local/bin:$PATH"

RUN pip install --no-cache-dir psycopg2 proto-parser && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --no-install-recommends curl gettext jq graphviz graphviz-dev procps netcat-traditional iputils-ping build-essential python3-dev \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libpq-dev python3-cffi && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN poetry config virtualenvs.create false

COPY pyproject.toml .
# COPY poetry.lock .

RUN poetry install

# RUN django-admin startproject dsg_example

# RUN python manage.py startapp async_example_bib_app