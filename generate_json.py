import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from pipelines import pipeline
import json
import sys
if __name__ == "__main__":
    if (len(sys.argv) > 1):
        d = dict()
        with open("data/"+str(sys.argv[1])) as file:
            input_string = file.read()
            nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", qg_format="prepend")
            l = nlp(input_string)
            for i in range(len(l)):
                d[i] = l[i]
        with open("data/questions.json", "w") as fp:
            json.dump(d, fp)
            
