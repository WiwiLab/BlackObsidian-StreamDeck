from pycaw.pycaw import AudioUtilities

print("Dispositivos de reproducción:\n")

for device in AudioUtilities.GetAllDevices():
    print(device)