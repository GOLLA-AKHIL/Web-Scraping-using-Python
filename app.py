from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default sample URL
    sample_url = "https://en.wikipedia.org/wiki/Web_scraping"
    url = sample_url  # Initialize url with sample_url

    if request.method == 'POST':
        url = request.form.get('url', sample_url)  # Get URL from form, default to sample_url

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting all paragraph texts from the page
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        return render_template('index.html', paragraphs=paragraphs, url=url)
    except requests.exceptions.RequestException as e:
        # If there was an error fetching the URL, render the error message
        return render_template('index.html', error=str(e), url=url)

if __name__ == '__main__':
    app.run(debug=True)
