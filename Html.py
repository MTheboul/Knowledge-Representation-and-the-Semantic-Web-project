from flask import Flask, url_for
app = Flask(__name__)

@app.route('/') #base page
def ontology_page():
    html  = """<html><body>"""
    html += """<div>"""
    html += """<span>Movie Quiz generator<span/>"""
    html += """<input placeholder="General topic here..."/>"""
    html += """<div/>"""

    html += """</body></html>"""
    return html



import werkzeug.serving
werkzeug.serving.run_simple("localhost", 5000, app)