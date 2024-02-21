from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 1,00,000'
    },
    {
        'id': 2,
        'title': 'Data Science',
        'location': 'Rawalpindi, Pakistan',
        'salary': 'Rs. 150,000'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'location': 'Remote, Pakistan',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Karachi, Pakistan',
        'salary': 'Rs. 110,000'
    },
    {
        'id': 5,
        'title': 'Frontend Engineer',
        'location': 'New York, USA',
        'salary': '$180,000'
    },
]

@app.route('/')
def hello_world():
    # return render_template('home.html')
    return render_template('main.html', jobs=JOBS,company_name='CareerComet')

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)
if __name__== "main":
    app.run(debug=True)    