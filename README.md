# API Mirror

A very simple testing utility that takes API calls to any endpoint, printing and returning the headers and body (if any). Originally used to test the proxy function of an API Gateway under development.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed, then run `pip3 install -r requirements.txt`. It is recommended to use a virtual environment.

### Running

To get up and running, simply clone the repo, ensure you have the prerequisites listed below installed, and then run `python3 run.py`.

The port(s) can be set by either changing the `PORTS` value in `config.py`, or by setting the `API_MIRROR_PORTS` environment variable. For example:
```bash
API_MIRROR_PORTS=8010 python3 run.py
```

*Note: Multiple ports can be specified with a comma-separated list. This spawns a thread for each port.*

### Example Usage

Once running, any calls you make to the given host and port will be mirrored back.

#### JSON

Request:
```bash
curl -X POST \
  'http://localhost:8010/path?key=value' \
  -H 'Content-Type: application/json' \
  -d '{ "test": "value" }'
```

Response:
```json
{
  "body": {
    "test": "value"
  },
  "form": null,
  "headers": {
    "Accept": "*/*",
    "Content-Length": "19",
    "Content-Type": "application/json",
    "Host": "localhost:8010",     
    "User-Agent": "curl/7.47.0"
  },
  "method": "POST",
  "path": "path",
  "query": {
    "key": "value"
  }
}
```

#### Form

Request:
```bash
curl -X DELETE \
  'http://localhost:8010/data' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'param1=value1&param2=value2'
```

Response:
```json
{
  "body": null,
  "form": {
    "param1": "value1",
    "param2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Content-Length": "27",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "localhost:8010",
    "User-Agent": "curl/7.47.0"
  },
  "method": "DELETE",
  "path": "data"
}
```

## Built With

* [Flask](http://flask.pocoo.org/)

## Authors

* [David Barrell](https://github.com/dabarrell) ([davidbarrell.me](https://www.davidbarrell.me/))

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
