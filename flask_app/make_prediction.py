import pickle
import pandas as pd
import numpy as np

# read in the model
object_model = pickle.load(open("rf_app_object_model.pickle", "rb"))
galaxy_model = pickle.load(open("rf_app_galaxy_model.pickle", "rb"))

# create a function to take in user-entered amounts and apply the model
def which_object(amounts_float):

    # make a prediction for the astronomical object class
    prediction = object_model.predict(pd.DataFrame([amounts_float]))[0]

    # determine galaxy type if output from previous model is 'GALAXY'
    if prediction == 'GALAXY':
    	prediction = galaxy_model.predict(pd.DataFrame([amounts_float]))[0]

    # fix output text
    if prediction == 'STAR':
    	prediction = 'Star'
    if prediction == 'QSO':
    	prediction = 'Quasar'
    if prediction == 1:
    	prediction = 'Spiral Galaxy'
    if prediction == 0:
    	prediction = 'Elliptical Galaxy'

    return prediction

# chooses an image to display based on the prediction above
def which_image(prediction):
    if prediction == 'Star':
        file = 'star_img.jpg'
    if prediction == 'Quasar':
        file = 'quasar_img.jpg'
    if prediction == 'Spiral Galaxy':
        file = 'spiral_img.jpg'
    if prediction == 'Elliptical Galaxy':
        file = 'elliptical_sdss.jpg'

    return file


