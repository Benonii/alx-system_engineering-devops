# Automate the task of creating a custom HTTP header response with puppet

# Class: nginx
# This class installs nginx, sets it up and adds a custom header
#
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx']
  }

  file { '/var/www/html/index.html':
    ensure  => 'present',
    content => 'Hello World!',
  }

  exec { 'start_server':
    command => '/usr/bin/sudo /bin/service nginx start',
  }

  exec { 'add_custom_header':
    command => "sed -i '29a add_header X-Served-By $hostname;' /etc/nginx/nginx.conf",
    path    => ['/usr/bin/', '/bin/'],
  }

  exec { 'restart_server':
    command => 'sudo service nginx restart',
    path    => ['/usr/bin/', '/bin/'],
  }
}
include nginx
