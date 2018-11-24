

.. image:: https://github.com/lennepkade/MuseoToolBox/raw/master/metadata/museoToolBox_logo_128.png
   :target: https://github.com/lennepkade/MuseoToolBox/raw/master/metadata/museoToolBox_logo_128.png
   :alt: MuseoToolBox logo


**Museo ToolBox** is a python library to simplify the use of raster/vector. One of the most important contributions is the interface between a cross-validation strategy and learning/predicting with Scikit-Learn. 

The other meaningful contribution is the **rasterMath** function which allow you to do whatever you like on a raster in a few lines : mean/modal/prediction/whittaker (you use your own function), and **rasterMath** manage everything : the nodata value, reading the raster block per block, saving to a new raster...

Who build Museo ToolBox ?
-------------------------

I am `Nicolas Karasiak <http://www.karasiak.net>`_\ , a Phd student at Dynafor Lab. I work on the identification of tree species throught dense satellite image time series with Sentinel-2. A special thanks to `Mathieu Fauvel <http://fauvel.mathieu.free.fr/>`_ who gave me the love of good and open-source coding.

What's the point ?
------------------

Today, the main usages of Museo ToolBox are :


* **vectorTools**

  * Create validation/training sets from vector, and Cross-Validation directly compatible with Scikit-Learn GridSearchCV. The aim is here to **promote the spatial validation/training** in order to lower spatial auto-correlation.
  * Extract each pixel centroid from polygons in order to have each band value to the vector,
  * and so extract values from raster to vector in order to learn model with only the vector

* **rasterTools**

  * Extract band value from vector ROI (polygons/points)
  * **rasterMath**\ , certainly the most useful for most of the users : allows you to do some math on your raster. Just load it, rasterMath will return you the value for each pixel (in all bands) and do whatever you want : predicting a model, signal treatment (whittaker, double logistic...), modal value, mean...

* **learnTools**

  * Based on Scikit-Learn. Still working on it...

That seems cool, but is there some help to use this ?
-----------------------------------------------------

I thought about Museo ToolBox as a tool to promote the use of spatial sampling (validation/training at least by stand) and to ease the way to compute Satellite Image Time Series, so of course I gave some help.

I build `several python notebooks to give you some nice tutorials : just go to the demo part of Museo ToolBox <https://github.com/lennepkade/MuseoToolBox/tree/demo/>`_.

How do I install it ?
---------------------

For now, I still don't build a pip package, so you have to clone this repository and to had it in your python path.

Why this name ?
---------------

As Orfeo ToolBox is one my favorite and most useful library to work with raster data, I choose to name my work as Museo because in ancient Greek religion and myth, `Museo is the son and disciple of Orfeo <https://it.wikipedia.org/wiki/Museo_(autore_mitico>`_\ ). If you want an acronym, let's say MUSEO means 'Multiple Useful Services for Earth Observation';