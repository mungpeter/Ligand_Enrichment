#!/usr/bin/perl -w

# Peter Ung  1 September 2007
# print out selected column(s) only, other columns ignored

die "\nUsage: x.pl <file> <column no.> ...
   eg: x.pl input.txt 2 3 1 5 4\n\n" 
  if @ARGV < 2; 

$file = shift @ARGV;
for (@ARGV) 
{ die "\n    Error: Entered <column no.> is/are not digit(s)\n\n" if /\D+/; }

open FILE, "< $file" 
  or die "\n    Errorr: File < $file > not found.\n\n";

while (<FILE>)
{
  @x = split;
  for ($a = 0; $a <= $#ARGV; $a++)
  {
    print $x[$ARGV[$a]-1] if $ARGV[$a] <= $#x+1;
    print "  " unless $a == $#ARGV;
    print "\n" if $a == $#ARGV;
  }
}
