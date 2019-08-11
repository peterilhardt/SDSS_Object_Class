from flask import Flask, request, render_template, url_for
from make_prediction import which_object, which_image

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_object page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_object/', methods = ['GET', 'POST'])
def render_message():

    # user-entered values
    properties = ['redshift', 'u-g', 'g-r']

    # error message to ensure correct input type
    message = [ "The entered amount must be a number.",
                "The entered amount must be a number.",
                "The entered amount must be a number."]

    # hold all amounts as floats
    amounts = []

    # takes user input and ensures it can be turned into a float
    for i, val in enumerate(properties):
        user_input = request.form[val]
        try:
            float_property = float(user_input)
        except:
            return render_template('index.html', message = message[i])
        amounts.append(float_property)

    # show user final message
    final_message = which_object(amounts)
    final_image = which_image(final_message)

    return render_template('index.html', message = final_message, 
                            image = final_image)


if __name__ == '__main__':
    app.run(debug=True)