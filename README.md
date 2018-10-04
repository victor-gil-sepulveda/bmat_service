# Test BMAT service

## Dependencies
flask, flask_restful, webargs

Install them using pip. E.g.

```bash
> sudo pip install flask
> sudo pip install flask_restful
> sudo pip install webargs
```

## Try it

Download this repository, put the path into your ```PYTHONPATH``` and run the service server with:

```bash
> python -m bmatservice.service.main
```

To attach it to any other ip/port use the ```--host``` and ```--port```. e.g. :
```bash
> python -m bmatservice.service.main --host 127.0.0.1 --port 5000
```

This will give you access to the REST get endpoint. You can try it with:

```bash
curl "http://127.0.0.1:5000/bmat/v1/rgroup?artist=65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab&sleep_time=0.5&limit=150&offset=50"
```

### Endpoint options
- sleep_time: A *Float* indicating the seconds that the server will wait between requests to BMAT API.  
- artist: A BMAT id (an uid *String*).  
- offset: A positive *Integer* telling the service the index of the first element we want to retrieve.
- limit: A positive *Integer* telling the service the maximum number of elements to be returned (range [50, 150])

## Considerations and criticisms

Most of the decisions I took had to do with the little time I had to finish the test, and I feel there is a lot of room for improvement.

- I think the code is quite self-explanatory, but more docstrings are needed.
- The testing coverage sucks.
- Maybe it is possible to get the release count in any other way. The implemented one is very inefficient.
- This README could be improved!