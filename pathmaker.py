import sys, os, errno
def makePath(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def makeFile(path):
  if os.path.exists(path) == False:
    file = open(path, 'w')
    file.close

def splitPath(path):
  folders = []
  while 1:
      path, folder = os.path.split(path)
      if folder != "":
          folders.append(folder)
      else:
          if path != "":
              folders.append(path)

          break
  folders.reverse()
  return folders

def parsePath(current_file, relative_path):
  curr_parts = splitPath(current_file)[:-1]
  rel_parts = splitPath(relative_path)
  for part in rel_parts:
    if part == '..':
      curr_parts = curr_parts[:-1]
    elif part !='.':
      curr_parts.append(part)
  return os.sep.join(curr_parts)[1:]

def makeFilePath(current_file, relative_path):
  newpath = parsePath(current_file, relative_path)
  split = os.path.split(newpath)
  makePath(split[0])
  if not os.path.splitext(relative_path)[1]:
    newpath = newpath + os.path.splitext(current_file)[1]

  makeFile(newpath)
  return newpath