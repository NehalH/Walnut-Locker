import inotify.adapters
import os

# path to the lock file
lock_file_path = "./lockfile.txt"

# path to the Unlock.py script
unlock_script_path = "./grant.py"

def is_file_locked(file_path):
    # check if the file is listed in the lock file
    with open(lock_file_path, "r") as lock_file:
        locked_files = lock_file.read().splitlines()
        return file_path in locked_files

def on_access_event(event):
    # check if the accessed file is locked
    if is_file_locked(os.path.join(event[2], event[3])):
        # run the Unlock.py script
        os.system(f"python3 {unlock_script_path}")

# create the inotify event listener
notifier = inotify.adapters.Inotify()
notifier.add_watch(".")

# listen for the ACCESS event
for event in notifier.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event
    if "IN_ACCESS" in type_names:
        print("Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        os.system(f"python3 {unlock_script_path}")
