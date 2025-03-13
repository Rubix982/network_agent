from setuptools import setup

setup(
    name="network_agent",
    version="1.0",
    packages=["network_agent"],
    install_requires=["requests", "streamlit", "pandas"],
    entry_points={"console_scripts": ["network-agent=network_agent.agent:start"]},
)
