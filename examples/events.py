# -*- coding: utf-8 -*-
from onvif import ONVIFCamera
__author__ = 'vahid'


if __name__ == '__main__':
    mycam = ONVIFCamera('172.16.0.60', 80, 'admin', 'P@55word') #, no_cache=True)
    #event_service = mycam.create_events_service()
    #print(event_service.GetEventProperties())

    pullpoint = mycam.create_pullpoint_service()
    #req=pullpoint.PullMessages({"Timeout":"PT10S", "MessageLimit":3})
    #print(req.CurrentTime, '--',req.TerminationTime, req.NotificationMessage)

    #pullpoint=event_service.CreatePullPointSubscription()
    #print(pullpoint.CurrentTime, '----', pullpoint.TerminationTime,'------',pullpoint.SubscriptionReference)

    event_service = mycam.create_events_service()
    pps = event_service.CreatePullPointSubscription()
    plp = mycam.pullpoint.zeep_client.create_service(
        '{http://www.onvif.org/ver10/events/wsdl}PullPointSubscriptionBinding',
        pps.SubscriptionReference.Address._value_1)
    pullmess = pullpoint.PullMessages({"Timeout":"PT10S", "MessageLimit":3})
    print(pullmess.NotificationMessage)


