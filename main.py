from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            .margin {{
                margin: 0 auto;
                width: 500px;
                display: block;
                margin: 0 auto;
                padding-top: 50px;
                top: 45%;
                left: 50%;
                width: 550px;
                height: 550px;
                display: block;
            }}
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                width: 100%;
                height: 175px;
                margin: 10px 0;
                font-size: 14px;
                border-radius: 4px;
                padding: 10px 15px;
                box-sizing: border-box;
            }}
            input[type=text], select {{
                width: 100%;
                margin: 10px 0;
                padding: 10px 15px;
                border-radius: 3px;
                display: inline-block;
                border: 2px solid;
                box-sizing: border-box;
            }}
            input[type=submit] {{
                width: 100%;
                color: white;
                border: none;
                margin: 10px 0;
                cursor: pointer;
                padding: 12px 15px;
                border-radius: 3px;
            }}
            .footer {{
                left: 0;
                bottom: 0;
                width: 100%;
                height: 50px;
                position: absolute;
            }}
            .footer p {{
                text-align: center;
                padding: 35px 0 0 0;
            }}
        </style>
    </head>
    <body>
        <div class="margin">
            <div>
                <h1>Web Caesar</h1>
                <p>Type in a message and the amount of rotation to see your message encrypted!</p>
                <hr>
                <form action ="/" method="POST">
                    <textarea name="text" placeholder="Enter Message to Encrypt:">{0}</textarea>
                    <label for "rot">Enter Amount to Rotate:</label>
                    <input type="text" id="rot" name="rot" value="0">
                    <input type="submit" value="Encrypt">
                </form>
            </div>
        </div>
        <div class="footer">
            <p class="footer">by Snehali Patel</p>
        </div>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    rot_text = str(request.form['text'])
    encrypt_text = rotate_string(rot_text, rot)
    return form.format(encrypt_text)

app.run()