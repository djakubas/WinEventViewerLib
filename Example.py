import WinEventViewerLib as wlog 

if __name__ == "__main__":

    #Add Source to Registry
    if wlog.Register_Event_Source("MyApp"):
        print("Source added to Registry")
    else:
        print("Failed to add Source to registry")
    
    #Prepare Event details
    source_name = 'MyApp'
    event_type = wlog.EVENTLOG_INFORMATION_TYPE
    data = ["Test event", "Additional information"]

    #Write Event
    if wlog.Write_Event(source_name=source_name,
                     event_type=event_type,
                     data=data):
        print("Event written succesfully")
    else:
        print("Failed to write event")
    
    #Get Events
    events = wlog.Get_Event_Logs()
    
    #Print latest Event
    if events:
        wlog.Print_Event(events[-1])