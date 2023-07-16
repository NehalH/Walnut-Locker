import inotify.adapters
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# path to the lock file
lock_file_path = os.path.join(script_dir, "data", "lockfile.txt")

# path to the Unlock.py script
unlock_script_path = os.path.join(script_dir, "grant.py")

def is_file_locked(file_path):
    # check if the file is listed in the lock file
    with open(lock_file_path, "r") as lock_file:
        locked_files = lock_file.read().splitlines()
        return file_path in locked_files

def on_write_event(event):
    # check if the written file is locked
    full_file_path = os.path.abspath(os.path.join(path,filename))
    print(full_file_path)
    if is_file_locked(full_file_path):
        # run the Unlock.py script
        os.system(f"python3 {unlock_script_path}")

# create the inotify event listener
notifier = inotify.adapters.Inotify()
notifier.add_watch("./test",mask=inotify.constants.IN_OPEN)

# listen for the WRITE event
for event in notifier.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event
    print('-')
    if "IN_OPEN" in type_names:
        on_write_event(event)
