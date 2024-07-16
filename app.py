from flask import Flask, render_template, request, url_for, jsonify
import random

app = Flask(__name__)


@app.route('/gifs')
def gifs():
    myGifs = (
        "https://giphy.com/clips/firstwefeast-hot-ones-first-we-feast-rhett-link-eat-the-worlds-spiciest-curry-JOAGMQg0GlPeKNCVIJ"
    )
    randomGif= random.choice(myGifs)
    return render_template('gifs.html', random=randomGif, randomBool=True, myGifs= myGifs)

@app.route('/input', methods=['GET', 'POST'])
def input():
    imgData={
        "dog": ["https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_3x2.jpg", "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*"],
        "cat" :["https://images.unsplash.com/photo-1529778873920-4da4926a72c2?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHx8MA%3D%3D"]
    }
    if request.method == 'POST':
        query = request.form['query']
        if query not in imgData:
            return "No data found for" + query
        return render_template('images.html',imgData=imgData[query])

    return render_template('input.html', url=url_for('input'))

if __name__== "__main__":
    app.run(host='0.0.0.0', port = 70, debug=True)