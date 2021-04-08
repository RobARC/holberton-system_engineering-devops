# Install and configure an Nginx server using Puppet instead of Bash

# apt-get update.
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}

# Install nginx
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

# Creates and sets the content of the "index.html" file.
file { 'index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Holberton School'
}

#Redirect to another file
file_line { 'Redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '        rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;'
}

# Restart service
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File_line['Redirection']
}
