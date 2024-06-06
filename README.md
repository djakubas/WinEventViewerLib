# WinEventViewerLib

WinEventViewerLib is a Python library for interacting with the Windows Event Viewer, allowing users to retrieve event logs, write events to the log and manipulates registry event sources.

# Prerequisites

To use WinEventViewerLib, you need to have the pywin32 library installed. You can install it using pip:

<code>pip install pywin32
</code>

# Notes
Ensure your script has the necessary permissions to access the Windows Event Viewer and modify the registry.
* Accessing and modifying the Windows Event Viewer requires read and write access to the event logs and may require administrative privileges.
* Registering and removing event sources involves writing to the Windows Registry, which typically requires administrative privileges.
* Writing events to the event log requires that the event source is already registered.
* Running scripts that interact with the Windows Event Viewer or registry may need to be executed with elevated permissions (Run as Administrator).
* For detailed usage of pywin32, refer to the PyWin32 Documentation.



