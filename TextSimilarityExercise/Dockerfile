FROM python:3.6-slim
COPY . /TextSimilarityExercise/src
COPY ./src /TextSimilarityExercise/src
WORKDIR /TextSimilarityExercise/src
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "SimilarityAPI.py" ]