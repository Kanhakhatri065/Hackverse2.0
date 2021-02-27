'''
    Distributive Compilation API server (app.py)
    @Author: Divakar Lakhera
    -> Provides API for front-end and back-end communication
'''

from flask import Flask
from flask_cors import CORS
from flask import jsonify, request
from serverSystem.pendingProcess import WorkerNode, InternalProcessList, BackNode
import concurrent.futures
from text import docs

app = Flask(__name__)
cors = CORS(app)

introStr = """Distributive Compilation Server 0.3 (beta) <br> Written By: Divakar Lakhera <br>
              For API usage visit  /apiref/
            """
globalProcessQueue = InternalProcessList()
currentNode = globalProcessQueue.currentServerNode


@app.route('/')
def hello_world():
    return introStr


@app.route('/stat/')
def ok():
    return jsonify({"status": "OK"})


@app.route('/api/add/', methods=['GET'])
def addJob():
    gitid = str(request.args['link'])
    workerNode = WorkerNode()
    workerNode.gitLink = gitid
    workerNode.userId = -1
    usrId = globalProcessQueue.addJob(workerNode)
    if usrId == -1:
        return jsonify({"status": "BAD", "id": str(usrId), "node": str(currentNode)})
    return jsonify({"status": "OK", "id": str(usrId), "node": str(currentNode)})


@app.route('/api/getJob/')
def returnNode():
    topNode = globalProcessQueue.getJob()
    if topNode == -1:
        return jsonify({"git": "None", "id": "None", "status": "None", "node": str(currentNode)})
    return jsonify({"git": str(topNode.gitLink), "id": str(topNode.userId), "node": str(currentNode)})


@app.route('/api/getStatus/', methods=['GET'])
def retStatus():
    uid = int(request.args['id'])
    nid = int(request.args['node'])
    if nid != currentNode:
        return jsonify({"node": str(currentNode)})
    return jsonify({"jobStatus": str(globalProcessQueue.getStatus(uid)), "node": str(currentNode)})


@app.route('/api/regHost/')
def getHostID():
    # not required Now
    hid = globalProcessQueue.addNewHost()
    return jsonify({"host": str(hid)})


@app.route('/api/jobDone/', methods=['GET'])
def jobDone():
    print(globalProcessQueue.registeredHost)
    hostID = int(request.args['host'])
    userID = int(request.args['user'])
    downLink = str(request.args['down'])
    reqNode = int(request.args['node'])
    if reqNode != currentNode:
        return jsonify({"status": "Wrong Node", "code": "9"})
    print(hostID)
    print(userID)
    print(downLink)
    bkNode = BackNode()
    bkNode.userId = userID
    bkNode.hostId = hostID
    bkNode.downLink = downLink
    retcode = globalProcessQueue.jobDone(bkNode)
    if retcode == -1:
        return jsonify({"status": "Unknown Job", "code": str(retcode)})
    if retcode == -2:
        return jsonify({"status": "Unknown Host", "code": str(retcode)})
    if retcode == -3:
        return jsonify({"status": "Too Slow, Already Committed", "code": str(retcode)})
    if retcode == 0:
        return jsonify({"status": "Done!! Points added", "code": str(retcode)})
    return jsonify({"status": "Server Error, Contact Admin", "code": "99"})


@app.route('/api/fetch/', methods=['GET'])
def getFetch():
    uid = int(request.args['user'])
    nodex = int(request.args['node'])
    if nodex != currentNode:
        return jsonify({"status": "W_Node", "code": "9"})
    stat = globalProcessQueue.getStatus(uid)
    if stat != 0:
        return jsonify({"status": "Not ready", "code": str(stat)})
    retNode = globalProcessQueue.getBackNodeFinal(uid)
    return jsonify(
        {"down": str(retNode.downLink), "host": str(retNode.hostId), "user": str(retNode.userId), "code": str(stat)})


# -----------------------
# Admin API starts here !
# ------------------------

@app.route('/api/admin/flush/', methods=['GET'])
def adminFlush():
    magic = str(request.args['magic'])
    print(magic)
    if magic == "pythonsucks":
        globalProcessQueue.flushAll()
        return jsonify({"status": "done xoxo"})
    return ""


@app.route('/api/admin/dump/', methods=['GET'])
def dump():
    magic = str(request.args['magic'])
    if magic != "pythonsucks":
        return ""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(globalProcessQueue.returnDump)
        return jsonify(future.result())


@app.route('/admin/poke')
def pokeServer():
    return jsonify({"node": currentNode})


# -----------------------
# Admin API ends here!
# ------------------------


@app.route('/apiref/')
def helpme():
    return docs


if __name__ == '__main__':
    app.run()
