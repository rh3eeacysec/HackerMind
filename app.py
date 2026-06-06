from flask import Flask, render_template, request, jsonify, session
from agents import agent_analyzer, agent_attacker, agent_defender, agent_reporter, agent_scorer
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "hackermind2026"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/analyst')
def analyst():
    return render_template('analyst.html')

@app.route('/defense')
def defense():
    return render_template('defense.html')

@app.route('/riskmap')
def riskmap():
    return render_template('riskmap.html')

@app.route('/api/analyze', methods=['POST'])
def run_analysis():
    data = request.get_json()
    system_description = data.get('system_description', '')
    
    if not system_description:
        return jsonify({'error': 'No system description provided'}), 400
    
    analysis = agent_analyzer(system_description)
    vulnerabilities = agent_attacker(analysis)
    defenses = agent_defender(vulnerabilities)
    report = agent_reporter(analysis, vulnerabilities, defenses)
    
    scores_raw = agent_scorer(analysis, vulnerabilities)
    try:
        scores = json.loads(scores_raw)
    except:
        scores = {
            "sql_injection": 75,
            "xss": 70,
            "auth_bypass": 80,
            "api_security": 65,
            "data_exposure": 85,
            "network_attack": 70
        }
    
    overall_risk = int(sum(scores.values()) / len(scores))
    
    return jsonify({
        'analysis': analysis,
        'vulnerabilities': vulnerabilities,
        'defenses': defenses,
        'report': report,
        'scores': scores,
        'overall_risk': overall_risk
    })

if __name__ == '__main__':
    app.run(debug=True)
