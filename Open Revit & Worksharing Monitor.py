import subprocess

#Insert directory path for Revit and Worksharing Monitor below.
def open_applications():
    application1_path = "C:\Directory\WorksharingMonitor.exe"
    application2_path = "C:\Directory\Revit.exe"

    subprocess.Popen(application1_path)
    subprocess.Popen(application2_path)

if __name__ == "__main__":
    open_applications()
