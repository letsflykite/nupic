# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

## This file defines parameters for a prediction experiment.

import os
from nupic.frameworks.opf.expdescriptionhelpers import importBaseDescription

# the sub-experiment configuration
config = \
{ 
  'modelParams': {
    'inferenceType': 'TemporalMultiStep',
    'clParams': { 
      'clVerbosity': 0,
      'steps': '1,2,3' 
    },
    'sensorParams': {
      'encoders': {
        'pitch': dict(
          fieldname = 'pitch',
          name = 'pitch',
          type = 'ScalarEncoder',
          minval = 0,
          maxval = 255,
          w = 3,
          resolution = 1)
        }, 
      'verbosity': 0,
    },
    'spParams': { },
    'tpParams': { }
  },
  'predictionSteps': [1, 2, 3]
}

mod = importBaseDescription('base_description.py', config)
locals().update(mod.__dict__)
