import subprocess

def run_backup(path):
    cmd = f"tar -czf /tmp/backup.tar.gz {path}"
    subprocess.Popen(cmd, shell=True)
