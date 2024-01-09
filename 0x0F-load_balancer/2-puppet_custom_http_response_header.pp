# Automate the process of creating a customized HTTP header response using Puppet
# The custom HTTP header needs to be named X-Served-By
# The hostname of the server where Nginx is operating should be the value of the custom HTTP header

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match => 'http {',
}
-> exec {'start':
  command => '/usr/sbin/service nginx start',
}

