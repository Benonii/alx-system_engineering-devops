# Puppet file for installing nginx on the webserver

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

  exec {'start_server':
    command => 'sudo service nginx start',
  }

  file { '/var/www/html/redirect.html':
    ensure  => 'present',
    content => 'Moved Permanently',
  }

  exec { 'modify_config':
    command => "sed -i '/server_name _;/a \tlocation /redirect_me {\n\troot var/www/html/;\n}\n' /etc/nginx/sites-available/default",
    path    => ['/bin', '/usr/bin'],
  }
}
include nginx
