"""
JARVIS Backend Server
API key workflow se inject hoti hai - safe & encrypted
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Workflow sed command se replace hoga
API_KEY = "GEMINI_API_KEY_PLACEHOLDER"

@app.route('/')
def home():
    return jsonify({"status":"JARVIS Online","message":"All systems operational"})

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_msg = data.get('message','')
        history = data.get('history',[])
        
        prompt = """You are J.A.R.V.I.S. from Iron Man. Work at "The Heaven Point" coaching, Shahganj, Prayagraj. Call user "Sir". Speak Hinglish. Be witty. Keep under 200 words. Info: Courses:CUET,NEET,JEE,SSC,Bank,Railway,Class3-12. Fees:₹1000-2500/mo. Contact:9044034585."""
        
        contents = [
            {"role":"user","parts":[{"text":prompt}]},
            {"role":"model","parts":[{"text":"At your service, Sir."}]}
        ]
        
        for msg in history[-8:]:
            contents.append({"role":msg.get("role","user"),"parts":[{"text":msg.get("text","")}]})
        
        contents.append({"role":"user","parts":[{"text":user_msg}]})
        
        resp = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}",
            json={"contents":contents,"generationConfig":{"temperature":0.9,"maxOutputTokens":400}},
            timeout=15
        )
        
        if resp.status_code == 200:
            ai_text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"response":ai_text,"status":"success"})
        else:
            return jsonify({"response":"Service unavailable. Call 9044034585.","status":"error"})
            
    except Exception as e:
        return jsonify({"response":"Error. Contact 9044034585.","status":"error"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
