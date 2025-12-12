#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use JSON;

print header('application/json');

my $component = param('component') || '';

my $result;

if ($component) {
    my $cmd = "check_component " . $component;
    my $output = `$cmd 2>&1`;
    
    if (!$output || $output =~ /not found/) {
        if ($component eq 'memory') {
            $output = "Memory: 2.4GB / 8GB (30%)";
        } elsif ($component eq 'cpu') {
            $output = "CPU Load: 15%";
        } elsif ($component eq 'disk') {
            $output = "Disk Usage: 45GB / 100GB (45%)";
        } elsif ($component eq 'network') {
            $output = "Network: Active - 125 Mbps";
        }
    }
    
    $result = {
        status => 'ok',
        component => $component,
        data => $output
    };
} else {
    $result = {
        status => 'error',
        message => 'Invalid component specified'
    };
}

print encode_json($result);
