pyproxy
=======

A simple HTTP proxy with plugin support

Documentation is coming soon, however, here is a brief overview of intended function:

* By default, the proxy only logs requests
  * In verbose mode, responses are also logged
* Plugins can alter proxy requests and responses, opening a variety of functions:
  * Changing request headers
  * Compressing the response before passing it to clients
  * Sending back a completely different file in the response
  * The list goes on..

The proxy doesn't bother with HTTPS requests, it lets them pass through unchanged, plugins can only block these requests, not modify them

The project is licensed under **The MIT License**
