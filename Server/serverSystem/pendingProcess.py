from random import randint
from threading import Thread, Lock


class WorkerNode:
    def __init__(self):
        self.gitLink = "."
        self.userId = -1
        # -1:Not Assigned 0: Ready 1: Busy 2: to-do 3: ready-to-flush
        self.status = -1


class BackNode:
    def __init__(self):
        self.downLink = "."
        self.userId = -1
        self.hostId = -1


class InternalProcessList:
    def __init__(self):
        self.internalJobQueue = {}
        self.userRegistered = set()
        self.todoNodes = []
        # self.takenByHost = set()
        self.size = 0
        self.justCommited = set()
        self.jobsDone = {}
        self.registeredHost = set()
        self.currentServerNode = randint(0, 100005)

    def flushAll(self):
        # Flush all the data-structures
        # ReInitialise All
        del self.internalJobQueue
        del self.userRegistered
        del self.todoNodes
        del self.justCommited
        # del self.takenByHost
        del self.jobsDone
        del self.registeredHost
        self.registeredHost = set()
        self.size = 0
        self.internalJobQueue = {}
        self.userRegistered = set()
        self.todoNodes = []
        # self.takenByHost = set()
        self.justCommited = set()
        self.jobsDone = {}

    def genID(self):
        # Warning 10^5 users only supported
        # FIX HERE !
        tempId = randint(0, 100005)
        iters = 0
        while tempId in self.userRegistered and iters < 10006:
            tempId = randint(0, 100005)
            iters += 1
        if tempId in self.userRegistered:
            return -1
        return tempId

    def genIDHost(self):
        # Warning 10^5 host only supported
        # FIX HERE !
        tempId = randint(0, 100005)
        iters = 0
        while tempId in self.registeredHost and iters < 10006:
            tempId = randint(0, 100005)
            iters += 1
        if tempId in self.registeredHost:
            return -1
        return tempId

    def addJob(self, node):
        usrid = self.genID()
        node.userId = usrid
        self.internalJobQueue[node.userId] = node
        self.userRegistered.add(node.userId)
        self.size += 1
        self.todoNodes.append(node.userId)
        return usrid

    def getStatus(self, userid):
        if userid not in self.userRegistered:
            return -1
        return self.internalJobQueue[userid].status

    def setStatus(self, userid, status):
        if userid not in self.userRegistered:
            return -1
        if status == 3:
            self.flushNode(userid)
            return
        self.internalJobQueue[userid].status = status

    def flushNode(self, userid):
        if userid not in self.userRegistered:
            return -1
        # add some validation !
        # usrToRemove = self.todoNodes.pop(0)
        self.userRegistered.remove(userid)
        del self.internalJobQueue[userid]
        self.justCommited.remove(userid)
        # self.takenByHost.remove(userid)

    def getJob(self) -> WorkerNode:
        if self.size == 0:
            return -1
        firstJob = self.todoNodes[0]
        return self.internalJobQueue[firstJob]

    def jobDone(self, backNode):
        if backNode.userId in self.justCommited:
            return -3
        # if backNode.hostId not in self.registeredHost:
        #   return -2
        # usr done remove from to-do
        if self.size == 0:
            return -3
        self.todoNodes.pop(0)
        # remove usr taken by host
        # self.takenByHost.remove(backNode.userId)
        # Set status to done by host
        self.setStatus(backNode.userId, 0)
        self.jobsDone[backNode.userId] = backNode
        self.justCommited.add(backNode.userId)
        self.size -= 1
        return 0

    def getBackNodeFinal(self, userId) -> BackNode:
        if userId not in self.userRegistered:
            return -1
        if userId not in self.justCommited:
            return -2
        retNode = self.jobsDone[userId]
        self.flushNode(userId)
        return retNode

    def addNewHost(self):
        newHID = self.genIDHost()
        self.registeredHost.add(newHID)
        return newHID

    def returnDump(self):
        outbuf = {}
        for i in self.userRegistered:
            outbuf[i] = self.internalJobQueue[i].gitLink
        for j in self.registeredHost:
            outbuf[j] = "<--HOST-->"
        outbuf[self.currentServerNode] = "<--Server Node-->"
        return outbuf

    def getServerNode(self):
        return self.currentServerNode
