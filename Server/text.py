docs = '''
    API Reference v1.4 (Beta)<br>
    Author: Divakar Lakhera <br>
    https://distributed-compiler.herokuapp.com/apiref/ <br>
    --------------------------------------------------------------<br>
    <br>
    <br>
    Whats New !<br>
    Usage of Host is depreciated, use host=0 everywhere. <br>
    On calling fetch(),jobDone(); server may return code 9.<br>
    Users need to loop again until code 9 gets removed. <br>
    <br>
    Frontend APIs<br>
    -----------------<br>
    <br>
    /api/add/?link=$(your github link)   => add new job into internal queue and returns unique session ID.<br>
    <br>
    /api/getStatus/?user=$(your id)&node=$(node) => returns status of the job by user with id<br>
    <br>
    /api/fetch/?user=$(your id)&node=$(node) => returns JSON {"down": $(download link), "host": $(host id), "user": $(user id)}
    <br>
    <br>
    Backend APIs<br>
    -----------------<br>
    <br>
    /api/regHost/  => returns unique host id for Host Compiler (Depreciated) <br>
    <br>
    /api/getJob/   => returns JSON {"git" :"<link>", "id" :"<user id>","node" :"<node id>"}<br>
    <br>
    /api/jobDone/?host="$(your host id)"&user=$(user id)&down="$(Download Link of ZIP)"&node=$(node id) => Tells server that the work is done and scoring is done.<br>
    ----------------------<br><br>
    Status:<br>
    -1 : Job not taken by anyone<br>
    0  : Job ready for user to download<br>
    1  : Job is begin processed by hosts<br>
    <br>
    Status for /api/jobDone/ :  <br>
    -1 : Unknown Job  (possible fix : check that userID is right and job is currently avail)<br>
    -2 : Unknown Host (possible fix : Register Your Host / Check your host ID is right) <br>
    -3 : Too Slow, Already Committed  (some other host completed the task before your system) <br>
     0 : GGWP !! You are the first one to complete the job. <br>
     9 : Wrong server cluster hit (Fix: Resend the request until code 9 gets removed.)<br>
    <br>
    <br>
    Other Info: <br>
    Host needs to get their unique ID first then start working else server will reject any work.<br>
    Jobs are scored in FCFS (first come basis)<br>
    '''
