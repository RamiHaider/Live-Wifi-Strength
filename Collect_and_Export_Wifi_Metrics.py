# First cell: Collecting and writing Wi-Fi metrics to a text file

import objc
import time

# Load the CoreWLAN framework
objc.loadBundle('CoreWLAN',
                bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                module_globals=globals())

# Get the CWInterface and CWWiFiClient classes
CWInterface = objc.lookUpClass('CWInterface')
CWWiFiClient = objc.lookUpClass('CWWiFiClient')

def get_wifi_status(interface_name='en0'):
    wifi_client = CWWiFiClient.sharedWiFiClient()
    interface = wifi_client.interface()
    
    if not interface:
        print(f"Interface {interface_name} not found.")
        return
    
    properties = [
        'rssiValue', 'noiseMeasurement', 'txRate', 'mcsIndex'
    ]
    
    wifi_status = {}
    for prop in properties:
        try:
            value = interface.valueForKey_(prop)
            wifi_status[prop] = value
        except Exception as e:
            wifi_status[prop] = f"Error: {str(e)}"
    
    return wifi_status

def collect_and_write_wifi_status():
    while True:
        wifi_status = get_wifi_status()
        if wifi_status:
            with open('wifi_metrics_output.txt', 'a') as file:
                file.write(f"{time.time()},{wifi_status['rssiValue']},{wifi_status['noiseMeasurement']},{wifi_status['txRate']},{wifi_status['mcsIndex']}\n")
        time.sleep(1)

# Start collecting and writing Wi-Fi status
collect_and_write_wifi_status()
