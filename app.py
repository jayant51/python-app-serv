from flask import Flask, jsonify, request
from waitress import serve


app = Flask(__name__)

@app.route('/')
def hello():
    return ('message: Remote VM execution')


@app.route('/restartvm')
def restartVM():
    #sshclnt = utils.getSSHClient()
	#s = sshclnt.get_transport().open_session()
	#paramiko.agent.AgentRequestHandler(s)
	#sshclnt.exec_command("sudo /sbin/reboot", get_pty=True)
	return ('message: Sent Restart remote server : services-uscentral.skytap.com')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
