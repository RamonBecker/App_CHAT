# App_CHAT
## :information_source: Information 

The chat implementation project was developed in the programming course with the Django framework promoted by Geek University. Redis software was used to communicate messages in real time. Web sockets were also used to carry out this communication.


## ⚠️ Prerequisite

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)

![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

## Demo

![chat](https://user-images.githubusercontent.com/44611131/118570436-8ca8b500-b752-11eb-9a01-988b730f3da5.png)

## ⚙️ Redis configuration

Upgrade your OS
```
sudo apt update
```
Then install redis
```
sudo apt install redis-server
```
After installation enter the redis configuration file
```
sudo nano /etc/redis/redis.conf
```
If line 127.0.0.1 :: 1 is commented on in the file, remove the comment and save the file. If it is not 127.0.0.1 :: 1 make this replacement and save the file to link to localhost.

Check if the port has been changed normally
```
sudo systemctl restart redis-server

```
## ⚙️ Creating virtual machine

Create your virtual machine
```
python3 -m venv venv
```
Activate your virtual machine
```
source venv/bin/activate
```
After the virtual machine is activated, install the project dependencies
```
pip install -r requirements.txt```
```



## :rocket: Installation

![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

```sh
git clone https://github.com/RamonBecker/App_CHAT.git
```

![](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)


```sh
git clone https://github.com/RamonBecker/App_CHAT.git
or install github https://desktop.github.com/ 

```

## :zap: Technologies	

- Python
- WebSockets
- Redis


## :memo: Developed features

- [x] The user can create his virtual room
- [x] The user can send a message inside his virtual room to other users

## :technologist:	 Author

By Ramon Becker 👋🏽 Get in touch!



[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/RamonBecker)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40'>](https://www.linkedin.com/in/https://www.linkedin.com/in/ramon-becker-da-silva-96b81b141//)
![Gmail Badge](https://img.shields.io/badge/-ramonbecker68@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ramonbecker68@gmail.com)

