from flask import Flask, jsonify, abort, render_template

from utils import DatasetNumber, special_join

app = Flask(__name__)



# Function to custom error message
@app.errorhandler(422)
def special_error_message(error):
    return render_template('snippets/errors.html', error=error),422


@app.route('/')
def home():
    '''
    This function only return a render_template to home page
    :return: template html
    '''
    return render_template('index.html')


def _number_position(value):
    '''
    Private function, receive a positive number and check the decomposition of that number.
    Using dict mapping method.

    :return: string with number converted to word
    '''

    if value < 20:
        return DatasetNumber.static_unity_mapping[value]
    if value < 100:
        return special_join(DatasetNumber.static_ten_mapping[value // 10],
                     DatasetNumber.static_unity_mapping[value % 10])
    if value < 1000:
        return special_join(DatasetNumber.static_hundred_mapping[value // 100],
                     DatasetNumber.static_ten_mapping[(value % 100) // 10],
                     DatasetNumber.static_unity_mapping[(value % 100) % 10])
    if value == 1000:
        return "Mil"
    else:
        value_ten = value % 1000
        value_hundred = value // 1000


        if value_hundred < 20:
            result_hundred = DatasetNumber.static_unity_mapping[value_hundred]
        else:
            result_hundred = special_join(DatasetNumber.static_ten_mapping[value_hundred // 10],
                                   DatasetNumber.static_unity_mapping[value_hundred % 10])

        result_ten = special_join(DatasetNumber.static_hundred_mapping[value_ten // 100],
                                DatasetNumber.static_ten_mapping[(value_ten % 100) // 10],
                                DatasetNumber.static_unity_mapping[(value_ten % 100) % 10])

        return '{} mil e {}'.format(result_hundred, result_ten)


@app.route('/<value>', methods=["GET"])
def get_number_extension(value):
    """ This method is main to receiver number write by user

    :var value: is number receive in user request
    :type string

    :return json with result
    """

    try:
        # convert string to int
        value = int(value)
    except:
        # exception case, value not is number
        return abort(422, 'Not possible convert string to integer.')


    # Checks whether the number is at the limit
    if value < -99999 or value > 99999:
        return abort(400, 'Please, enter with number between -99999 and 99999')

    if value < 0:
        value = abs(value)
        result_data = 'menos {}'.format(_number_position(value))
    elif value == 0:
        result_data = "zero"
    else:
        result_data = _number_position(value)

    result = {'extenso': result_data}

    #lib jsonify convert result to JSON and return reponse to user
    return jsonify(result)



if __name__ == '__main__':
    app.run()
