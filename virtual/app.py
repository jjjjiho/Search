from flask import Flask, jsonify, render_template, request
app=Flask(__name__)

@app.route('/')
def call_API():
    return render_template('search.html')

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)