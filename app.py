<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jenkins Job Trigger</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            padding: 20px;
        }
        .button {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center">Trigger Jenkins Job</h1>
        <form id="jobForm">
            <div class="mb-3">
                <label for="jenkinsUrl" class="form-label">Jenkins URL</label>
                <input type="text" class="form-control" id="jenkinsUrl" placeholder="Enter Jenkins URL" required>
            </div>
            <div class="mb-3">
                <label for="jobName" class="form-label">Job Name</label>
                <input type="text" class="form-control" id="jobName" placeholder="Enter Job Name" required>
            </div>
            <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" placeholder="Enter Username" required>
            </div>
            <div class="mb-3">
                <label for="token" class="form-label">Token</label>
                <input type="text" class="form-control" id="token" placeholder="Enter Token" required>
            </div>
            <div class="mb-3">
                <label for="parameterName" class="form-label">Parameter Name</label>
                <input type="text" class="form-control" id="parameterName" placeholder="Enter Parameter Name" required>
            </div>
            <div class="mb-3">
                <label for="parameterValue" class="form-label">Parameter Value</label>
                <input type="text" class="form-control" id="parameterValue" placeholder="Enter Parameter Value" required>
            </div>
            <button type="submit" class="btn btn-primary button">Trigger Job</button>
        </form>
        <div id="result" class="mt-3"></div>
    </div>

    <script>
        document.getElementById('jobForm').addEventListener('submit', async function(event) {
            event.preventDefault();

            const jenkinsUrl = document.getElementById('jenkinsUrl').value;
            const jobName = document.getElementById('jobName').value;
            const username = document.getElementById('username').value;
            const token = document.getElementById('token').value;
            const parameterName = document.getElementById('parameterName').value;
            const parameterValue = document.getElementById('parameterValue').value;

            const response = await fetch('/trigger-job', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    jenkinsUrl,
                    jobName,
                    username,
                    token,
                    parameters: {
                        [parameterName]: parameterValue
                    }
                })
            });

            const result = await response.text();
            document.getElementById('result').innerText = result;
        });
    </script>
</body>
</html>
