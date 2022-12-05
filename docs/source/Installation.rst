Getting Started
===============

To get the *HEACalculator* local copy up and running, follow these
simple steps:

Prerequisites
-------------

The *HEACalculator* only requires the following packages:

-  numpy
-  PyQt5
-  Typer

Installation
------------

Clone the repo
~~~~~~~~~~~~~~

.. code:: sh

   git clone https://github.com/dogusariturk/HEACalculator.git

Change Directory
~~~~~~~~~~~~~~~~

.. code:: sh

   cd HEACalculator

Install virtualenv via pip
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   pip install virtualenv

Create a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   virtualenv venv

Activate the virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  For UNIX-based systems

   .. code:: sh

      source bin/activate

-  For Windows-based systems:

   -  If using the default command prompt (``cmd``), type:

   ::

          .\venv\Scripts\activate

   -  If using Windows PowerShell (``PS``), type:

   ::

          .\venv\Scripts\Activate.ps1

Install HEACalculator
~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   pip install .