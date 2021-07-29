import os
import numpy as np

from flask import render_template
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from tensorflow.keras.preprocessing import image
from keras.models import load_model


# Create the website object
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # Website initialization
    if request.method == 'GET':
        return render_template('index.html')

    # if request.method == 'POST':
    else:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # if not select file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # Check if it is an image file
        if not allowed_file(file.filename):
            flash(f'Allowed file extensions: {str(ALLOWED_EXTENSIONS)}')
            return redirect(request.url)

        # When the user uploads a file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Load image and scale it
    test_image = image.load_img(os.path.join(UPLOAD_FOLDER, filename), target_size=(224, 224))
    test_image = image.img_to_array(test_image) / 255.0
    test_image = np.expand_dims(test_image, axis=0)

    # Predict uploaded image to website
    model = app.config['MODEL']
    cls_index = model.predict_classes(test_image)
    cls_result = CATEGORIES[cls_index[0]]

    img_path = os.path.join("/", UPLOAD_FOLDER, filename)
    return render_template('index.html',
                           img_path=img_path,
                           prediction=str(cls_result.title())
                           )


def main():
    # Load trained model
    model = load_model(TRAINED_MODEL)

    # Make configurations
    app.config['SECRET_KEY'] = 'secret'
    app.config['MODEL'] = model

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB upload limit
    app.run()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":

    CATEGORIES = ['bear', 'butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse',
                  'leopard', 'lion', 'panda', 'sheep', 'spider', 'squirrel', 'wolf', 'zebra']

    # Allowed file extensions
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Trained model
    TRAINED_MODEL = 'saved_model.h5'

    # for website uploads
    UPLOAD_FOLDER = 'static/uploads'

    main()
