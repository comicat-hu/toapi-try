from toapi import Api
from items.joblist import Joblist
from settings import MySettings

api = Api('https://www.104.com.tw', settings=MySettings)
api.register(Joblist)

if __name__ == '__main__':
    api.serve()

