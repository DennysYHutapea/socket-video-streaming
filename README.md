# video-streaming

simple video streaming server & client based on: [Developing a Live Video Streaming Application using Socket Programming with Python](https://medium.com/nerd-for-tech/developing-a-live-video-streaming-application-using-socket-programming-with-python-6bc24e522f19)



### TODO

- [ ] [ERROR] connectionabortederror 10053



### how to install

I strongly recommend you to work inside a virtual environment.

```
$ pip install -r requirements.txt
```



### how to run

run server

```
$ python server.py --video {videopath}
```



and then run client on a separate bash

```
$ python client.py
```

