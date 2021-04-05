# kill process killmenow
exec { 'killmenow':
    path    => '/usr/bin/',
    command => 'pkill -9 killmenow'
}  
