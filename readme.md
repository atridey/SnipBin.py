# SnipBin.py

A Python API wrapper for [SnipBin](http://snip.hxrsh.in/)

## Setup

```sh
pip install snipbin.py
```

## Usage

Before starting, familiarize yourself with the [SnipBin API Docs](http://snip.hxrsh.in/api-docs.md)
Start by importing the package into your program. Here it is being imported as such:
```py
from snipbin import snipbin
```
Note that I'm importing a class called `snipbin`. If you instead choose to import the entire library, remember that any functions being called below are methods inside of this class.

### Authorize

If you would like to use account restricted features of SnipBin, pass your API key here. However, you don't have to if you don't plan on using restricted features.
```py
#With authorization
sb = snipbin('Please do not put your real API key in GitHub readmes')
#Without authorization
sb = snipbin()
```

## Functions

### Fetching Snips

Required arguements: slug
Optional arguements: none
Positional order: slug
This does not work on encrypted snips
```py
sb.fetch('oUVnB')
#Returns: {'id': 61, 'slug': 'oUVnB', 'createdAt': '2022-02-25T20:47:22.820Z', 'content': 'Thanks for using SnipBin.py!', 'password': None, 'language': 'C#', 'authorId': 4}
```

### Creating Snips

Required arguements: slug, content, language
Optional arguements: password
Positional order: slug, content, language, password
To automatically find the language of text, use the detect language function
If you would like the snip to be linked with an account, pass an API key in the authorization step
```py
sb.create(slug = 'ri9yL', content = """print('Hello World!')""", language = 'Python')
#Returns: {'id': 64, 'slug': 'ri9yL', 'createdAt': '2022-02-25T20:57:49.710Z', 'content': "print('Hello World!')", 'password': None, 'language': 'Python', 'authorId': 4}
```

### Editing Snips

Required arguements: slug
Optional arguements: content, newslug, password
Positional order: slug, content, newslug, password
You must have authorization for the account linked to a snip to edit it
```py
sb.edit(slug = '46BXz', content = """console.log("This snip has been edited")""")
#Returns: {'id': 66, 'slug': '46BXz', 'createdAt': '2022-02-25T21:04:35.543Z', 'content': 'console.log("This snip has been edited")', 'password': None, 'language': 'TypeScript', 'authorId': 4}
```

### Deleting Snips

Required arguements: slug
Optional arguements: none
Positional order: slug
You must have authorization for the account linked to a snip to delete it
```py
sb.delete(slug = 'sy_gB')
#Returns: {'id': 67, 'slug': 'sy_gB', 'createdAt': '2022-02-25T21:10:24.757Z', 'content': 'cout << "This snip no longer exists" << endl;', 'password': None, 'language': 'C++', 'authorId': 4}
```

### Detecting Languages

Required arguements: snippet
Optional arguements: none
Positional order: snippet
```py
sb.detect_lang(snippet = """printf("What language is this code?")""")
#Returns: {'data': 'C'}
```

# Acknowledgements

Thanks to [Harsh](http://github.com/harshhhdev), the creator of SnipBin, for helping me use his API and giving me tips for this wrapper.
