http://www.toapi.org/
https://github.com/gaojiuli/toapi

run with python3.6
flask framework
XPath

--

docker image (amazonlinux install toapi with python3.6)

https://hub.docker.com/r/comi/amazonlinux-toapi/

--

python36
pip-3.6

--

ec2 amazonlinux ami install python3.6

* sudo yum update -y
* sudo yum -y groupinstall development
* sudo yum install python36 python36-virtualenv python36-pip

python -V (check version)

--

install toapi

* sudo pip-3.6 install toapi

--

run toapi

* toapi new myapi (new toapi template)
* toapi run -a 0.0.0.0:5000 (default run on 127.0.0.1:5000)

--

setting ajax true need phantomjs

https://www.vultr.com/docs/how-to-install-phantomjs-on-ubuntu-16-04

--