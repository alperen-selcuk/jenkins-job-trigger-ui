from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger-job', methods=['POST'])
def trigger_job():
    data = request.json
    jenkins_url = f"{data.get('jenkins_url')}/job/{data.get('job_name')}/buildWithParameters"
    auth = (data.get('username'), data.get('token'))
    params = {'replicas': data.get('replicas')}
    
    try:
        response = requests.post(jenkins_url, auth=auth, params=params)
        response.raise_for_status()  # Hata varsa raise yapar
        return jsonify({'message': 'Jenkins job triggered successfully'}), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error triggering Jenkins job: {e}")
        return jsonify({'message': 'Failed to trigger Jenkins job', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

