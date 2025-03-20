import os

base_dir = os.getcwd() + "/home/barrel/manusmcp/tools/.data"
base_next_dir = os.getcwd() + "/home/barrel/manusmcp/tools/.next"
proxy_url = os.getenv("PROXY_URL", None)
hf_token = os.getenv("HF_TOKEN", None)
omni_parser_client_url = os.getenv("OMNI_PARSER_CLIENT_URL", "ginigen/OmniParser-v2-pro")
