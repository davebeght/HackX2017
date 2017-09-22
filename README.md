# genkon_app

## Installation

*NOTE: Requires [python3](https://www.python.org/download/releases/3.0/),*
[Node.js](http://nodejs.org/)

* `$ git clone https://github.com/jonasrothfuss/genkon_app.git`
* `$ cd genkon_app/`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

## Docker
* `$ sudo docker build ./`
* `$ sudo docker images` (lists docker images ... find image that was just created -> my_image)
* `$ sudo docker tag my_image $DOCKER_ID_USER/my_image`
* push docker image to docker hub repo: `$ sudo docker push $DOCKER_ID_USER/my_image`
* pull docker image on host machine: `$ sudo docker pull $DOCKER_ID_USER/my_image`
* run the container: `$ sudo docker run -p 8000:8000 $DOCKER_ID_USER/my_image`
