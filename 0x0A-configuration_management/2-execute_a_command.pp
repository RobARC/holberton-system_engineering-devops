#create a manifest that kills a process named killmenow.
exec { "Kill":
 command => 'usr/bin/pkill -9 killmenow',
}  
