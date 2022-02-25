import requests
import json

class snipbin:
    def __init__(self, key = None):
        self.key = key

    
    def fetch(self, slug): 
        return requests.get(f'http://snip.hxrsh.in/api/snip/{slug}').json()

    def detect_lang(self, snippet):
        payload = json.dumps({'snippet': snippet})
        #return requests.post('http://snip.hxrsh.in/api/detect', headers = {'Content-Type': 'application/json'}, data = f"""{{"snippet":"{snippet}"}}""").json()
        return requests.post('http://snip.hxrsh.in/api/detect', headers = {'Content-Type': 'application/json'}, data = payload).json()

    def create(self, slug, content, language, password = None):
        headers = {'Content-Type': 'application/json', 'Authorization': self.key}
        payload = json.dumps({'content': content, 'language': language, 'slug': slug, 'password': password})
        return requests.post('http://snip.hxrsh.in/api/snip/new', headers = headers, data = payload).json()

    def delete(self, slug):
        headers = {'Content-Type': 'application/json', 'Authorization': self.key}
        return requests.delete(f'http://snip.hxrsh.in/api/snip/{slug}/delete', headers = headers).json()

    def edit(self, slug, content = None, newslug = None, password = None):
        headers = {'Content-Type': 'application/json', 'Authorization': self.key}
        dictionary = {}
        if newslug != None:
            dictionary['slug'] = newslug
        if content != None:
            dictionary['content'] = content
        if password != None:
            dictionary['password'] = password
        payload = json.dumps(dictionary)
        return requests.put(f'http://snip.hxrsh.in/api/snip/{slug}/edit', headers = headers, data = payload).json()