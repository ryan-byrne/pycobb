Installation
------------

Using PIP:

.. code-block:: console

  pip install pycobb

From Source:

.. code-block:: console

  git clone https://github.com/ryan-byrne/pycobb
  cd pycobb
  python setup.py install

Quickstart
----------

Let's start by printing every pitch Clayton Kershaw threw in 2020.

This can be done in a python script:

.. code-block:: python

  import pycobb
  pitches = pycobb.get(pitchers=['Clayton Kershaw'], years=[2020])
  print(pitches)

Or directly from the command line:

.. code-block:: console

  pycobb -p "Clayton Kershaw" -y 2020 --print

.. toctree::
 :maxdepth: 2
