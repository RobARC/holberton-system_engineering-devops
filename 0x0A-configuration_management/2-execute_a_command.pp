#create a manifest that kills a process named killmenow.
exec { 'Kill':
 command  => 'pkill -f killmenow',
 path     => 'usr/bin/',
 user     => 'root',
 provider => 'shell',

}  
