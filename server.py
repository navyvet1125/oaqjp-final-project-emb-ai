""" This file is the entry point for the server. """
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("EmotionDetectionAPI")

@app.route('/')
def home():
    """
        This function is used to render the home page of the API.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
        This function is used to analyze the emotion of 
        a given text using the Watson Emotion Analysis API.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions == "<b>Invalid text! Please try again!</b>" :
        return emotions, 400
    result = "For the given statement, the system response is "
    result += "'anger': " + str(emotions['anger']) + ", "
    result += "'disgust': " + str(emotions['disgust']) + ", "
    result += "'fear': " + str(emotions['fear']) + ", "
    result += "'joy': " + str(emotions['joy']) + " and "
    result += "'sadness': " + str(emotions['sadness']) + ". "
    result += "The dominant emotion is <b>" + str(emotions['dominant_emotion']) + "</b>."
    return result, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
