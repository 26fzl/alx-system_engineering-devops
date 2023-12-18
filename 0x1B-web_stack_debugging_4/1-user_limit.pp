# OS configuration 
exec { 'configuration_user_hard_limits':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
exec { 'configuration_user_soft_limits':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
