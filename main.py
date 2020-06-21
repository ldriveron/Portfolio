from app_files import app  # import the flask app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5252')  # run the app
    # app.run(debug = True)
