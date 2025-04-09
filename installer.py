import os
osutildir = os.getenv("APPDATA", "/appdata").replace('\\', '/') + "/../LocalLow/osutil"
os.mkdir(osutildir)
