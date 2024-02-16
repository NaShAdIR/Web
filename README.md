# **Web**  
A simple web framework for creating simple web applications.  
### **Project structure:**  
```
MySite
├── run.py
├── app1
|   ├── __init__.py
|   ├── urls.py
|   └── views.py 
├── MySite
|   ├── __init__.py
|   ├── settings.py
└── └── asgi.py
```
---

- run.py
```python
from web import Setup

if __name__ == '__main__':
    setup = Setup()
    setup.run()
```
---

- MySite/settings.py
```python  
DEBUG = True # False
TRACING = True # False

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 80

INSTALL_APPS = [
    'app1',
    'app2',
    'app_n'
]

STATIC_FILE_DIRS = {
    'app_1': [
        ('', '/frontend')
    ]
}

ROOT_URLPATTERNS = [
    ('', 'app1'), # (url, app_name)
    ('app2/', 'app2') 
]
```
---

- MySite/asgi.py
```python  
from web.core.asgi import asgi_app

app = asgi_app()
```
---

