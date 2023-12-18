# web server setup

exec { 'Fix_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
