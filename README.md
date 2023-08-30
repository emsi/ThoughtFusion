# ThoughtFusion
Two AI agents talking and improving asnwer

1. Clone the project
1. Create a file `openai_api_key.txt` with your OpenAI API key
1. RUN:
```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. streamlit run thoughtfusion/webui/app.py --browser.gatherUsageStats false
```
