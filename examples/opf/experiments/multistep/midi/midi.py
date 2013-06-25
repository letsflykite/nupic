"""A simple client to create a CLA model for midi music."""

from csv import reader
import datetime

from nupic.frameworks.opf.modelfactory import ModelFactory

import description

def createModel():
  return ModelFactory.create(description.config)

def run():
  # Model setup
  song_length = 160
  song_iterations = 40
  headers = ['pitch']
  model = createModel()
  model.enableInference({'predictionSteps': range(1, song_length + 1),
                         'predictedField': 'pitch'})

  # Read in file
  records = [record for record in reader(open('legdam10_parsed.txt'))]

  # Train CLA
  gen_outputs_on = (5, 10, 20, 30, 40, )
  result = 0
  print "Training"
  for i in range(1, song_iterations + 1):
    for (j, record) in enumerate(records):
      print "Iteration: %i, Record: %i" % (i, j)

      modelInput = dict(zip(headers, record))
      modelInput["pitch"] = float(modelInput["pitch"])
      result = model.run(modelInput)
    if i in gen_outputs_on:
      print "Generating output on iteration", i
      predictions = result.inferences['multiStepBestPredictions']
      f = open('multistep_output_%i.txt' % i, 'w')
      for step in range(1, song_length + 1):
        print predictions[step]
        f.write(str(predictions[step]) + '\n')
      f.close()

if __name__ == "__main__":
  run()
