import os
import requests
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def call_azure(system_prompt, user_prompt, max_tokens=800):
    url = f"{AZURE_ENDPOINT}openai/deployments/{AZURE_DEPLOYMENT}/chat/completions?api-version=2025-01-01-preview"
    print("Calling URL:", url)
    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "api-key": AZURE_KEY
        },
        json={
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": 0.7
        },
        timeout=60
    )
    data = response.json()
    print("AZURE RESPONSE:", data)
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    elif "error" in data:
        return f"Error: {data['error']['message']}"
    return "No response from AI"

def agent_analyzer(system_description):
    return call_azure(
        "You are a system analyzer. Analyze the given system and identify what it is, its components, and its attack surface. Be specific and structured.",
        f"Analyze this system: {system_description}",
        max_tokens=1000
    )

def agent_attacker(system_analysis):
    return call_azure(
        "You are an ethical hacking expert. Based on the system analysis, identify potential vulnerabilities and attack vectors step by step. Think like a hacker.",
        f"Find vulnerabilities in this system: {system_analysis}",
        max_tokens=1000
    )

def agent_defender(vulnerabilities):
    return call_azure(
        "You are a cybersecurity defense expert. For each vulnerability identified, provide specific defense strategies and security controls.",
        f"Provide defenses for these vulnerabilities: {vulnerabilities}",
        max_tokens=1000
    )

def agent_reporter(analysis, vulnerabilities, defenses):
    from datetime import date
    today = date.today().strftime("%B %d, %Y")
    return call_azure(
        f"You are a security report writer. Today's date is {today}. Create a clear, structured security report based on the analysis, vulnerabilities and defenses provided. Always include a complete summary section at the end. Use today's date in the report.",
        f"Create a security report from:\nAnalysis: {analysis}\nVulnerabilities: {vulnerabilities}\nDefenses: {defenses}",
        max_tokens=2000
    )

def agent_scorer(analysis, vulnerabilities):
    return call_azure(
        """You are a security scoring expert. Return ONLY a JSON object with these exact keys and integer scores from 0-100:
{"sql_injection": 0, "xss": 0, "auth_bypass": 0, "api_security": 0, "data_exposure": 0, "network_attack": 0}
Return ONLY the JSON, nothing else. No explanation, no markdown, no backticks.""",
        f"Score these vulnerabilities:\nAnalysis: {analysis}\nVulnerabilities: {vulnerabilities}",
        max_tokens=200
    )
