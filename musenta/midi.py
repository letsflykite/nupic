"""A simple client to create a CLA model for midi music."""

import csv
import datetime

from nupic.frameworks.opf.modelfactory import ModelFactory

import base_description

def createModel():
  return ModelFactory.create(base_description.config)

def run():
  model = createModel()
  model.enableInference({'predictionSteps': range(5),
                         'predictedField': 'pitch'})
  with open ('legdam10_parsed.txt') as fin:
    reader = csv.reader(fin)
    headers = reader.next()
    print headers
    print reader.next()
    print reader.next()
    for record in reader:
      print record
      modelInput = dict(zip(headers, record))
      modelInput["pitch"] = float(modelInput["pitch"])
      result = model.run(modelInput)
      print result

if __name__ == "__main__":
  run()
