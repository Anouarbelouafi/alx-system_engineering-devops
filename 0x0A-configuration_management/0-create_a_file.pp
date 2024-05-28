#The code will create a file name school inside the /tmp Directory

file { '/tmp/school':
    path    => '/tmp/school',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    }
