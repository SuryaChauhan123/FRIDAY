from pycaw.pycaw import AudioUtilities

def control_volume(percent):
    """
    Set system volume.
    percent: 0-100
    """

    device = AudioUtilities.GetSpeakers()
    volume = device.EndpointVolume

    # Convert percentage to scalar (0.0 - 1.0)
    volume.SetMasterVolumeLevelScalar(percent / 100.0, None)

    print(f"Changed volume to {percent}, sir.")

