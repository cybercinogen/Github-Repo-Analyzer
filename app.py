from flask import Flask, request, jsonify
from flask_cors import CORS
from github_api import get_repo_info, get_contributors, get_commit_activity
from utils import parse_github_url

# Create a new Flask application instance
app = Flask(__name__)
# Enable CORS support for the application
CORS(app)

# --- ROUTES ---

# Define a route for retrieving repository metadata
@app.route('/api/repo-info', methods=['POST'])
def repo_info():
    """
    Returns repository metadata for the given GitHub repo URL.

    Expects a JSON payload with a 'repo_url' key containing the GitHub repository URL.
    Returns a JSON response with the repository metadata or an error message.
    """
    # Get the JSON payload from the request
    data = request.json
    # Extract the repository URL from the payload
    repo_url = data.get('repo_url')
    # Parse the repository URL to extract the owner and repository names
    owner, repo = parse_github_url(repo_url)
    # Validate the repository URL
    if not owner or not repo:
        # Return an error response if the URL is invalid
        return jsonify({'error': 'Invalid GitHub repository URL'}), 400
    # Retrieve the repository metadata
    result, error = get_repo_info(owner, repo)
    # Handle any errors that occurred during metadata retrieval
    if error:
        # Return an error response if an error occurred
        return jsonify({'error': error}), 400
    # Return the repository metadata as a JSON response
    return jsonify(result)

# Define a route for retrieving a list of contributors
@app.route('/api/contributors', methods=['POST'])
def contributors():
    """
    Returns a list of contributors for the given GitHub repo URL.

    Expects a JSON payload with a 'repo_url' key containing the GitHub repository URL.
    Returns a JSON response with the list of contributors or an error message.
    """
    # Get the JSON payload from the request
    data = request.json
    # Extract the repository URL from the payload
    repo_url = data.get('repo_url')
    # Parse the repository URL to extract the owner and repository names
    owner, repo = parse_github_url(repo_url)
    # Validate the repository URL
    if not owner or not repo:
        # Return an error response if the URL is invalid
        return jsonify({'error': 'Invalid GitHub repository URL'}), 400
    # Retrieve the list of contributors
    result, error = get_contributors(owner, repo)
    # Handle any errors that occurred during contributor retrieval
    if error:
        # Return an error response if an error occurred
        return jsonify({'error': error}), 400
    # Return the list of contributors as a JSON response
    return jsonify(result)

# Define a route for retrieving weekly commit activity
@app.route('/api/commit-activity', methods=['POST'])
def commit_activity():
    """
    Returns weekly commit activity for the given GitHub repo URL.

    Expects a JSON payload with a 'repo_url' key containing the GitHub repository URL.
    Returns a JSON response with the commit activity data or an error message.
    """
    # Get the JSON payload from the request
    data = request.json
    # Extract the repository URL from the payload
    repo_url = data.get('repo_url')
    # Parse the repository URL to extract the owner and repository names
    owner, repo = parse_github_url(repo_url)
    # Validate the repository URL
    if not owner or not repo:
        # Return an error response if the URL is invalid
        return jsonify({'error': 'Invalid GitHub repository URL'}), 400
    # Retrieve the commit activity data
    result, error = get_commit_activity(owner, repo)
    # Handle any errors that occurred during commit activity retrieval
    if error:
        # Return an error response if an error occurred
        return jsonify({'error': error}), 400
    # Return the commit activity data as a JSON response
    return jsonify(result)

# Run the application if this script is executed directly
if __name__ == '__main__':
    # Run the application on host '0.0.0.0' and port 5000 in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)
