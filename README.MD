Test assignment for Apollo


Tutorial project files in
>caesar/

All test assignment files in
>assignment/

Exact configurations for each task provided in appropriate task folder

To simulate  AWS serverless used local docker-compose file   

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