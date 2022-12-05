Usage
=====

Command Line Interface
----------------------

Calling ``HEACalculator`` without any option/argument will show the help
text.

.. figure:: https://user-images.githubusercontent.com/46679086/205514909-ab4930cd-2f5b-4d9c-9598-750c661d44db.png

Currently, *HEACalculator* supports two different calculation methods.

-  ``HEACalculator search single <ALLOY>`` calculates all
   parameters/predictions for the given ALLOY and exports the results to
   the stdout (i.e., terminal)

.. figure:: https://user-images.githubusercontent.com/46679086/205514947-ca25fb25-c726-4de9-a79b-1cccf354b4e3.png

-  ``HEACalculator search range`` calculates all parameters/predictions
   for a given composition range of a given set of elements and exports
   results to the stdout (i.e., terminal) by default.

.. figure:: https://user-images.githubusercontent.com/46679086/205514952-95dcb909-2147-4fcf-91df-4e0d1a1321dc.png

-  ``--csv`` flag can be used with ``HEACalculator search range``
   command to make Range Search function to export the results in CSV
   format to the stdout or redirected to a file using the ``>``
   operator.

Graphical User Interface
------------------------

.. figure:: https://user-images.githubusercontent.com/46679086/205514915-e4ce2dbf-4636-4639-b978-3a018183ba82.png

-  Start Graphical User Interface (GUI) ``sh  HEACalculator gui``

-  Select elements from the periodic table

-  Enter the requested at% values in the table at the corresponding cell

-  Click *Calculate* button

-  Click *Save* button to save the calculated values as a CSV file