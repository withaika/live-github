#!/usr/bin/env python
import os,hashlib as h,sys,base64 as b64,zlib,json as j,argparse as arg,itertools as it,string as s,time as t
try:
  settings={}
  read=[i for i in zlib.decompress(b64.b64decode(open("settings","r").read())).split("\n")]
  for i in range(len(read)):
    settings[read[i].split('*')[0]]=read[i].split('*')[1]
except IOError:
  if len(sys.argv)<4:
    sys.exit("""GitHub Live Folder:
    --path     <base directory>  : Path to clone to (will create live folder within this one) (default: current path)
    --url      <clone url>       : GitHub clone url
    --branch   <branch to push>  : Branch to clone from and push to (default: master)
    --comment  <comment>         : Default comment for commits (default: "Commit at <timestamp>")
    --username <github username> : Login username (Will store locally unencrypted)
    --password <github password> : Login password (Will store locally unencrypted)

Flags without defaults are required for setup.""")
  args={}
  for i in range(len(sys.argv[1::2])):
    args[sys.argv[1::2][i].lower().strip('-')]=sys.argv[2::2][i].lower()
  for i in ['path','url','username','password','branch','comment']:
    if not args.has_key(i):
      if i=="username" or i=="password" or i=="url":
        sys.exit("%s is required. Please use --%s <%s> flag and try again."%(s.capwords(i),i,i))
      else:
        if i=='path':args['path']=os.getcwd()
        if i=='branch':args['branch']='master'
        if i=='comment':args['comment']='Commit at {curtime}'##.format(curtime=str(int(t.time())))
  with open("settings",'w') as f:
    f.write(b64.b64encode(zlib.compress('basedir*%s\ngiturl*%s\nuser*%s\npass*%s\nbranch*%s\ndefcomm*%s'%(args['path'],args['url'],args['username'],args['password'],args['branch'],args['comment']))))

def dirHash(directory):
  SHAhash = h.md5()
  if not os.path.exists (directory):
    return -1
  try:
    for root, dirs, files in os.walk(directory):
      for names in files:
        filepath = os.path.join(root,names)
        try:
          f1 = open(filepath, 'rb')
        except:
          f1.close()
          continue
    while 1:
      buf = f1.read(4096)
      if not buf : break
      SHAhash.update(h.md5(buf).hexdigest())
      f1.close()
  except:
    import traceback
    traceback.print_exc()
    return -2
  return SHAhash.hexdigest()

while True:
  break

##clone
##add
##commit
##pull
##add
##commit
##pull
