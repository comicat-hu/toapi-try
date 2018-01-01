from toapi import Item, XPath

class Joblist(Item):
    jobName = XPath('//article/@data-job-name')
    jobNo = XPath('//article/@data-job-no')
    custName = XPath('//article/@data-cust-name')
    custNo = XPath('//article/@data-cust-no')
    area = XPath('//ul[@class="b-list-inline b-clearfix job-list-intro b-content"]/li[1]/text()')
    url = XPath('//a[@class="js-job-link "]/@href')

    class Meta:
        source = XPath('//article[@data-jobsource]')
        route = {'/joblist/?page=:page': '/jobs/search/?page=:page'}

