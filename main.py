from flask import Flask
from alice_scripts import Skill, request, say, suggest

import config

app = Flask(__name__)
skill = Skill(__name__)

@skill.script
def run_script():


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cur_host = config.HOST_IP
    port = 5000

    skill.run(host=cur_host, port=5000,
              ssl_context=(config.ssl_cert, config.ssl_priv), debug=False)
