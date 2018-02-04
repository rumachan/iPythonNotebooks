Display data for Raoul Island crater lakes for monitoring temperature and water level.

**raoul_lakes_longterm.ipynb**
- this is a replacement for a script that previously ran daily under cron and used a mish mash of different tool to produce data and plots
- it updates a file of daily mean values and plots the data

**raoul_lakes_recent.ipynb**
- allows you to select the 'last n days' of data, which are then plotted
- data are decimated from 1 sps to 1 spm (60s sampling)
- this is intended to be a user friendly alternative to http://images.geonet.org.nz/volcano/ki/glkz/40/drum.png, http://images.geonet.org.nz/volcano/ki/glkz/80/drum.png, and http://images.geonet.org.nz/volcano/ki/glkz/81/drum.png

