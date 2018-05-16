nudity
=======
.. image:: https://travis-ci.org/canaydogan/nudity.svg?branch=master
    :target: https://travis-ci.org/canaydogan/nudity
    :alt: Build status

About
-----
Nudity detection with re-trained Tensorflow MobileNet Model. Accuracy is 92.2% based on my dataset. Give it a try: http://nudity.canaydogan.net

Installation
------------
.. code-block:: sh

    $ pip install nudity


Requirements
------------
* Python3.5+

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
