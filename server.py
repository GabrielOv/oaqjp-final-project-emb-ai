from flask import Flask, render_template, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask(__name__)

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route('/emotionDetector')
def get_emotion_detection():
    requested_text = request.args.get('textToAnalyze')
    formated_response = emotion_detector('I love this')
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()


if __name__ == "__main__":
    run_emotion_detection()