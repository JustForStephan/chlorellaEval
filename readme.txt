The ClorellaEval algorithm
--------------------------

The population development of chlorella algaes is a very complex issue, which depends on several factors like the CO2-intensity of the ambient, the avaiability of water, the temperature and the light intensity.
To figgure out the effect of different dependency factors, goal is to implement a AI.

This AI is using a dataset to adapt the weights for every specific factor.
After training, the AI should be able to simulate the population of chlorellas with different factors.


The dataset is structured like this:

factor 1 | factor 2 | factor 3 | population growth
---------------------------------------------------
23       |546       |32542     |        2
54       |-1        |-23       |        -10
         |          |          |
         
         
