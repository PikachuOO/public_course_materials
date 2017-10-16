#!/usr/bin/perl -w

$current_count = 0;
$current_species = "";

while ($line = <STDIN>) {
	if ($line =~ /(\d+)\s*(.+)\s*$/) {
		$count = $1;
		$species = $2;
		if ($species eq $current_species) {
			$current_count += $count;
		} else {
			print "$current_count $current_species\n" if $current_count;
			$current_count = $count;
			$current_species = $species;
		}
	} else {
		print "Sorry couldn't parse: $line\n";
	}
}

print "$current_count $current_species\n" if $current_count;
