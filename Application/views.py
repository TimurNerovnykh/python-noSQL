from django.shortcuts import render
from Application2.models import CouchDBSession, MongoDBSession, CassandraDBSession


def home(request):
    return render(request, 'home.html')

def exec_req(request):
    if request._post['dbs'] == 'cdb':
        res = CouchDBSession.exec_query(request._post['req'])
    elif request._post['dbs'] == 'casdb':
        res = CassandraDBSession.exec_query(request._post['req'])
    else:
        res = MongoDBSession.exec_query(request._post['req'])

    return render(request, 'home.html', {'res': res})