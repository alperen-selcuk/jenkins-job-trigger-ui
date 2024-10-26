from flask import Flask, request, jsonify, render_template
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger-job', methods=['POST'])
def trigger_job():
    data = request.json
    jenkins_url = data.get('jenkinsUrl')
    job_name = data.get('jobName')
    username = data.get('username')
    token = data.get('token')

    # Dinamik parametreleri al
    parameters = data.get('parameters', {})

    # Jenkins job URL'i oluştur
    job_url = f"{jenkins_url}/job/{job_name}/buildWithParameters"

    # Jenkins job'u çalıştırmak için POST isteği gönder
    try:
        response = requests.post(
            job_url,
            auth=HTTPBasicAuth(username, token),
            params=parameters
        )

        if response.status_code == 201:
            return "Job triggered successfully!", 200
        else:
            return f"Failed to trigger job: {response.status_code} - {response.text}", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
