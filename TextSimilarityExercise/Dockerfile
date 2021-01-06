FROM python:3.6-slim
COPY . /src
COPY ./src /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "SimilarityAPI.py" ]