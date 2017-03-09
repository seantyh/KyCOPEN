#from rest_framework import viewsets
from django.http import HttpResponse
#from django.http import JsonResponse --> works for django > 1.7
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import throttle_classes, api_view
from rest_framework.response import Response
from misc.mongo import mongoDB
from models import Ptt
from serializers import PttSerializer
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
import json
import time

def ip_throttle(ip_args):    
    def deco_func(func):
	def wrapper(*args, **kw):
	    try:
                ip_buckets = ip_args[0]
		req = args[0]
		if len(ip_buckets) > 10:
		    ip_buckets = ip_buckets[1:]
		req_ip = req.META.get("REMOTE_ADDR")
		last_req_t = ip_buckets.get(req_ip, 0)
		if time.time() - last_req_t < 5:                
		    ip_buckets[req_ip] = time.time()
		    return HttpResponse(jsonDump({"status": "too frequent"}), status = 429)
		else:
		    return func(*args, **kw)
	    except Exception as ex:
		return HttpResponse(jsonDump({"status": "rate limit exception", "msg": str(ex)}), status = 500)
	return wrapper
    return deco_func

ip_records = []
def jsonDump(dic):
    return json.dumps(dic, ensure_ascii=False, indent=4)
    

# @api_view(['GET'])
def test(request):
    return HttpResponse(jsonDump({'status':'ok'}))

# @api_view(['GET'])
@ip_throttle([ip_records])
def concordance(request, query):
    return Response(query)
#    if request.method == 'GET':
#        return HttpResponse(request.user)
#        return HttpResponse(json.dumps({'test':'ok'}), content_type="application/json")

#    return HttpResponse('ok')
#    res = mongoDB('PTT', board)
#    if request.method == 'GET':
#        pttcon = []
#        for r in res.find({}, {'_id':0, 'post_time':1, 'title':1, 'content':1}).limit(10):
#            tmp = Ptt(r["post_time"],r["title"],r["content"])
#            pttcon.append(tmp)
#        serializedList = PttSerializer(pttcon, many=True)
#        return Response(serializedList.data)

from cwm.copensTools import getKeyness, getThesaurus, getSketch
from cwm.forms import DB_CHOICE

@ip_throttle([ip_records])
def keyness(request, query, tar_corp):
    database = DB_CHOICE 
    res = getKeyness(query, tar_corp, database)
    return HttpResponse(jsonDump(res), content_type="application/json")
    return HttpResponse(jsonDump(res))


from rest_framework.pagination import PaginationSerializer
from django.core.paginator import Paginator

@ip_throttle([ip_records])
def thesaurus(request, word):    
    res = getThesaurus(word)

#    paginator = Paginator(res, 2)
##    page = paginator.page(1)
#    page = paginator.page(int(request.GET.get('page', '1')))
#    serializer = PaginationSerializer(instance=page, context={'request':request})
    return HttpResponse(jsonDump(res))
    return Response(serializer.data)



# @throttle_classes([UserRateThrottle])
# @api_view(['GET'])
@ip_throttle([ip_records])
def sketch(request, query):
    res = getSketch(query)

    return HttpResponse(jsonDump(res), content_type="application/json")
    return HttpResponse(res, content_type="application/json")
