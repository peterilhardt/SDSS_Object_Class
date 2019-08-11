## Files:

1. `main.py` - The main code that uses Flask and calls make_prediction.py to run the model prediction with user's input
2. `make_prediction.py` - A separate script that reads in the models and defines a function to make a classification prediction 
3. `rf_app_object_model.pickle` - The random forest model for identification of astronomical object (qalaxy, quasar, or star)
4. `rf_app_galaxy_model.pickle` - The random forest model for identification of galaxy type (spiral or elliptical)
5. `index.html` (in a templates folder) - The webpage that takes in inputs for the model and outputs a result on the webpage (with styling)
