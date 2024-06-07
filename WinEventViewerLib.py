from win32evtlog import EVENTLOG_SEQUENTIAL_READ, EVENTLOG_FORWARDS_READ,EVENTLOG_INFORMATION_TYPE,EVENTLOG_ERROR_TYPE,EVENTLOG_WARNING_TYPE,ReadEventLog,OpenEventLog,CloseEventLog,GetNumberOfEventLogRecords
from win32evtlogutil import AddSourceToRegistry, ReportEvent,RemoveSourceFromRegistry

def Register_Event_Source(source_name, log_type='Application'):
    #Register a new event source in Windows Registry

    try:
        AddSourceToRegistry(source_name,None,log_type)
        return True
    except:
        return False

def Remove_Event_Source(source_name,log_type='Application'):
    #Removes an event source from Windows Registry
    try:
        RemoveSourceFromRegistry(source_name,log_type)
        return True
    except:
        return False

def Get_Total_Logs(server='localhost', log_type='Application'):
    log_handle = OpenEventLog(server, log_type)
    total = GetNumberOfEventLogRecords(log_handle)
    CloseEventLog(log_handle)
    return total

def Get_Event_Logs(server='localhost', log_type='Application'):
    #Get events from WinEventViewer

    log_handle = OpenEventLog(server, log_type)

    flags = EVENTLOG_FORWARDS_READ | EVENTLOG_SEQUENTIAL_READ
    events = []

    while True:
        records = ReadEventLog(log_handle, flags, 0)
        if not records:
            break
        for record in records:
            event = {
                'EventID': record.EventID,
                'ComputerName': record.ComputerName,
                'SourceName': record.SourceName,
                'TimeGenerated': record.TimeGenerated.Format(),
                'EventCategory': record.EventCategory,
                'EventType': record.EventType,
                'EventData': record.StringInserts
            }
            events.append(event)

    CloseEventLog(log_handle)

    return events

def Print_Event(event):
    #Prints event
    print(f"EventID: {event['EventID']}")
    print(f"ComputerName: {event['ComputerName']}")
    print(f"SourceName: {event['SourceName']}")
    print(f"TimeGenerated: {event['TimeGenerated']}")
    print(f"EventCategory: {event['EventCategory']}")
    print(f"EventType: {event['EventType']}")
    if event['EventData']:
        for i, data in enumerate(event['EventData']):
            print(f"EventData[{i}]: {data}")
    print('-' * 40)

def Write_Event(source_name, event_id=0, event_type=EVENTLOG_INFORMATION_TYPE, category=0, data=None):
    # Write an event to WinEventViewer
    try:
        ReportEvent(source_name,event_id,category,event_type,data)
        return True
    except:
        return False



