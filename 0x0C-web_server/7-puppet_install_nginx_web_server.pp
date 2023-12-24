# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80;
      server_name _;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 /;
      }
    }
  ",
  notify => Service['nginx'],
}

# Enable Nginx service and start it
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasstatus  => true,
  hasrestart => true,
}