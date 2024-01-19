import subprocess

def open_applications():
    # Using raw strings for Windows paths
    application1_path = r"C:\Directory\WorksharingMonitor.exe"
    application2_path = r"C:\Directory\Revit.exe"

    try:
        subprocess.Popen(application1_path)
        subprocess.Popen(application2_path)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    open_applications()
