FROM python:3.6-slim
COPY ./TextSimilarityExercise /TextSimilarityExercise
COPY ./TextSimilarityExercise/src /TextSimilarityExercise/src
COPY requirements.txt /TextSimilarityExercise/src
WORKDIR /TextSimilarityExercise/src
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "SimilarityAPI.py" ]