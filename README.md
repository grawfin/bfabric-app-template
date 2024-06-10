# bfabric-app-template
Template Application for Bfabric Webapp Concept (written in Python3) 

## Deployment 

1) Fork the Repo 

2) Clone your Repo

``` 
git clone https://github.com/your/bfabric-app-template/fork.git && cd bfabric-app-template
```

3) Install bfabricpy: 

```
git clone https://github.com/fgcz/bfabricPy.git && cd bfabricPy
git checkout bfabric12 
cd bfabricPy
python3 setup.py sdist && pip3 install dist/bfabric-0.13.*.tar.gz
cd ..
```

4) Set up virtual environment and install dependencies:
``` 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

5) Run the application 

```
python3 index.py
```

6) Check it out! 

Visit http://localhost:8050 to see your site in action.