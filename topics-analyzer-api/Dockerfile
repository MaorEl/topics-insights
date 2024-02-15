FROM python:3.12

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

# Don't change this port - streamlit default port is 8501
EXPOSE 8501

CMD streamlit run streamlit_app.py