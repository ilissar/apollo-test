Test assignment for Apollo


Test assignment files in
>assignment/

Tutorial project files in 
>caesar/

To start GUI run
>./gradlew run

and select from appropriate folder
>configuration.xml

```
Docker images build with open-faas.
Run .../openfaas/build.sh
```

For debug change in openfaas/template/python3-flask/Dockerfile value to:
```
ENV fprocess="python -u index.py"
```