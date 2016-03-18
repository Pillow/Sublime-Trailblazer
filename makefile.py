import sys, os, errno
class PathMaker:

  def __init__(self, current_file, relative_path):
    self.current_file = current_file
    self.relative_path = relative_path

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

  def parsePath():
    curr_parts = splitPath(self.current_file)[:-1]
    rel_parts = splitPath(self.relative_path)
    for part in rel_parts:
      if part == '..':
        curr_parts = curr_parts[:-1]
      elif part !='.':
        curr_parts.append(part)
    return os.sep.join(curr_parts)[1:]

  def makeFilePath():
    newpath = parsePath(self.current_file, self.relative_path)
    split = os.path.split(newpath)
    makePath(split[0])
    makeFile(newpath)