"""A simple client to create a CLA model for midi music."""

import csv
import datetime

from nupic.frameworks.opf.modelfactory import ModelFactory

import description

numLearningSteps = 1600
numStepsToPredict = 160

def createModel():
  return ModelFactory.create(description.config)

def run():
  model = createModel()
  model.enableInference({'predictionSteps': range(1, 160),
                         'predictedField': 'pitch'})
  with open ('legdam10_parsed.txt') as fin:
    reader = csv.reader(fin)
    headers = reader.next()
    print headers
    print reader.next()
    print reader.next()
    for i, record in enumerate(reader):
      if i == numLearningSteps:
        print result
        import pdb; pdb.set_trace()
        break
      print record
      modelInput = dict(zip(headers, record))
      modelInput["pitch"] = float(modelInput["pitch"])
      result = model.run(modelInput)
      print result

if __name__ == "__main__":
  run()
