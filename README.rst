nudity
=======

About
-----
Nudity detection with re-trained Tensorflow MobileNet Model. Accuracy is 98.2% based on my dataset

Installation
------------
from pip::

    $ pip install nudity


Requirements
------------
* Python3+

Usage
-----
via command-line

.. code-block:: sh

    $ nudity --image=IMAGE_FILE

via Python Module

.. code-block:: python

    from nudity import Nudity
    nudity = Nudity();
    print(nudity.has('/file/path/example.jpg'))
    # gives you True or False
    print(nudity.score('/file/path/example.jpg'))
    # gives you nudity score 0 - 1
