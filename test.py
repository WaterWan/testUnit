# coding=utf-8
import urllib, urllib2, sys
import json
import ssl
import sys

#TODO 代码写的太丑了，需要改一改
reload(sys)
sys.setdefaultencoding('utf8')

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# ak = "KUAVfmy1cyv8KSPyxQB0jOjk"
# sk = "dXjYgwGS89XIYdLIfpNdx1eblXl0qbMt"
ak = "vD2v2WFMzTLW5sE0mZhysG6y"
sk = "f7QRdfxMKD6DuE01fBDG3lOyWnfjLZv3"
# request_add = "https://aip.baidubce.com/rpc/2.0/solution/v1/unit_utterance"
request_add = "https://aip.baidubce.com/oauth/2.0/token?grant_type="
host = request_add + "client_credentials&client_id=" + ak + "&client_secret=" + sk
# https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6e386ba72b4f4bf99b3d95d7b9860faf&client_secret=6eb734a1250743fd93051a851fb647cb
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
# if content:
#     print(content)

content_json = json.loads(content)
access_token = content_json["access_token"]
print access_token

url = 'https://aip.baidubce.com/rpc/2.0/solution/v1/unit_utterance?access_token=' + access_token
ques = u'周六有雨吗'.encode('utf8')
post_data = "{\"scene_id\":8809,\"query\":\"" + ques + "\",\"session_id\":\" \"}"
request = urllib2.Request(url, post_data)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print(content)


