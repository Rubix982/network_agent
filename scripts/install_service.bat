schtasks /create /tn "NetworkAgent" /tr "python3 C:\code\network_agent\network_agent/agent.py" /sc onstart /rl highest
