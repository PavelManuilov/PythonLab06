import datetime
import re


def dt(pstr):
    '''
    приводит дату из трёх форматов к одному формату
    :param pstr: дата в формате datetime, str(yyyy-mm-dd hh24:mi:ss) или str(yyyy.mm.dd hh24:mi:ss)
    :return: возвращает дату в формате (oracle) yyyy.mm.dd hh24:mi:ss
    '''

    #print(type(pstr))
    #print(pstr)
    if type(pstr) is str:
        if re.match(r'^\d{2,4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$', pstr):
          xdt = datetime.datetime.strptime(pstr,'%Y-%m-%d %H:%M:%S')
        if re.match(r'^\d{2,4}\.\d{1,2}\.\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}$', pstr):
          xdt = datetime.datetime.strptime(pstr, '%Y.%m.%d %H:%M:%S')
    else:
        xdt=pstr

    #print(type(xdt))
    #print(xdt)
    return xdt.strftime('%Y.%m.%d %H:%M:%S')
