#create a manifest that kills a process named killmenow
exec { '/usr/bin/env pkill -9 killmenow':
}  
