Input file

gene1 1
gene1 2
gene2 3
gene2 4
gene5 5

output 

gene1 1,2
gene2 2,3
gene5 5

#####################Perl program#################
my $file="data.txt";
open(FH, "<", $file) or die ("error");
my %key_hash;
while($line=<FH>)
{
@arr=split(" ",$line);

push @{$key_hash{$arr[0]}},$arr[1];
}
for $key (keys (%key_hash))
{ 
$data="";
@key_value=@{$key_hash{$key}};


 if (scalar(@key_value>1))
	 {
		 $data=join(",",@key_value);
			print "$key $data \n";
			break;
	 }
	 else
	 {$data=$key_value[0];
	print "$key $data \n";
	break;
	 }
	  
} 



 
 
 
 
 
 
 


