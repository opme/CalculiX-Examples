#!/opt/conda/bin/python
import os
import multiprocessing
import shutil


# Provide access to the helper scripts
def modify_path():
    scripts_dir = os.path.dirname(__file__)
    while not 'Scripts' in os.listdir(scripts_dir):
        scripts_dir = os.path.abspath(os.path.join(scripts_dir, '..'))
    scripts_dir = os.path.join(scripts_dir, 'Scripts')
    if not scripts_dir in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + scripts_dir
    print('\nPATH = {}\n'.format(os.environ['PATH']))


# Move new files and folders to 'Refs'
def move(old_snap):
    new_snap = os.listdir(os.curdir)
    if not os.path.exists('Refs'):
        os.mkdir('Refs')
    for f in new_snap:
        if not f in old_snap:
            fname = os.path.basename(f)
            new_name = os.path.join(os.curdir, 'Refs', fname)
            if os.path.isfile(new_name):
                os.remove(new_name)
            if os.path.isdir(new_name):
                shutil.rmtree(new_name)
            os.rename(f, new_name)


if __name__ == '__main__':

    # Enable multithreading for ccx
    os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

    # Explicitly move to example's directory
    os.chdir(os.path.dirname(__file__))

    # Run the example
    modify_path()
    snap = os.listdir(os.curdir)
    os.system("cgx -bg pre.fbl")
    os.system("ccx modal")
    os.system("cgx -bg shapes.fbl")
    move(snap)
