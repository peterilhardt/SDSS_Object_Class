# Classifying Astronomical Objects from the Sloan Digital Sky Survey
---

This project aimed to classify astronomical objects identified by the Sloan Digital Sky Survey (SDSS), a multi-year effort to map and image the galaxies and stars encompassing nearly a quarter of the night sky. Approximately 3.5 million labelled galaxies, stars, and quasars were queried from the SDSS SciServer catalog along with their locations (given in declination and right ascension), IDs, and light properties (e.g. magnitudes of light from different regions of the spectrum as separated by photometric filters). All data were obtained from [SDSS Data Release 15](https://www.sdss.org/dr15/) and extracted via the web-based [CasJobs interface](https://skyserver.sdss.org/casjobs/) for easy integration with Python and Jupyter Notebook tools. Queried observations were temporarily stored in a postgreSQL database hosted by Amazon EC2. After obtaining the filtered data and an initial exploratory investigation, classification models were built using `scikit-learn` to predict an object's class using measured redshift values and magnitudes for the u, g, r, i, and z photometric filters. In addition, results from the [Galaxy Zoo project](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo) - compiled by the SDSS - were included to further classify galaxies as either spiral or elliptical according to the same measured predictors. The files presented in this repository include:

* *get_data.ipynb*: the procedure used to query data from the SDSS SciServer catalog (code largely derived from the [SciScript-Python repository](https://github.com/sciserver/SciScript-Python))
* *make_db.sql*: the SQL commands used to generate a postgreSQL database and tables hosting the SDSS data
* *connect_import_db.ipynb*: the procedure used to connect to the AWS EC2 instance and query data from the postgreSQL database
* *EDA.ipynb*: initial exploratory data analysis of the dataset
* *classification_object_types.ipynb*: the procedure used to build and evaluate classification models for object type classification (star, galaxy, quasar)
* *classification_galaxy_types.ipynb*: the procedure used to build and evaluate classification models for galaxy type classification (spiral, elliptical)
* *classification_model_evaluation.py*: functions for evaluating classification models, including calculation of performance metrics and generation of confusion matrices and ROC curves

Also included is the code and template for an interactive Flask application that allows users to input a redshift value, u-g color, and g-r color to obtain a prediction of the object type. 
